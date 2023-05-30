"""
Archivo - Documentos v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_arc_documentos, get_arc_documento
from .schemas import ArcDocumentoOut, OneArcDocumentoOut

arc_documentos = APIRouter(prefix="/v3/arc_documentos", tags=["archivo"])


@arc_documentos.get("", response_model=CustomPage[ArcDocumentoOut])
async def listado_arc_documentos(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    ubicacion: str = None,
):
    """Listado de documentos"""
    if current_user.permissions.get("ARC DOCUMENTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_arc_documentos(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            ubicacion=ubicacion,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@arc_documentos.get("/{arc_documento_id}", response_model=OneArcDocumentoOut)
async def detalle_arc_documento(
    current_user: CurrentUser,
    db: DatabaseSession,
    arc_documento_id: int,
):
    """Detalle de una documento a partir de su id"""
    if current_user.permissions.get("ARC DOCUMENTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        arc_documento = get_arc_documento(db, arc_documento_id)
    except MyAnyError as error:
        return OneArcDocumentoOut(success=False, message=str(error))
    return OneArcDocumentoOut.from_orm(arc_documento)
