"""
Archivo - Remesas Documentos v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_arc_remesas_documentos, get_arc_remesa_documento
from .schemas import ArcRemesaDocumentoOut, OneArcRemesaDocumentoOut

arc_remesas_documentos = APIRouter(prefix="/v3/arc_remesas_documentos", tags=["archivo"])


@arc_remesas_documentos.get("", response_model=CustomPage[ArcRemesaDocumentoOut])
async def listado_arc_remesas_documentos(
    current_user: CurrentUser,
    db: DatabaseSession,
    arc_documento_id: int = None,
    arc_remesa_id: int = None,
):
    """Listado de documentos de remesas"""
    if current_user.permissions.get("ARC REMESAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_arc_remesas_documentos(
            db=db,
            arc_documento_id=arc_documento_id,
            arc_remesa_id=arc_remesa_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@arc_remesas_documentos.get("/{arc_remesa_documento_id}", response_model=OneArcRemesaDocumentoOut)
async def detalle_arc_remesa_documento(
    current_user: CurrentUser,
    db: DatabaseSession,
    arc_remesa_documento_id: int,
):
    """Detalle de una documento de remesa a partir de su id"""
    if current_user.permissions.get("ARC REMESAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        arc_remesa_documento = get_arc_remesa_documento(db, arc_remesa_documento_id)
    except MyAnyError as error:
        return OneArcRemesaDocumentoOut(success=False, message=str(error))
    return OneArcRemesaDocumentoOut.from_orm(arc_remesa_documento)
