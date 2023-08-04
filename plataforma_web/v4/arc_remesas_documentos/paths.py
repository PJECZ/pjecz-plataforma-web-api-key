"""
Archivo - Remesas Documentos v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_arc_remesa_documento, get_arc_remesas_documentos
from .schemas import ArcRemesaDocumentoOut, OneArcRemesaDocumentoOut

arc_remesas_documentos = APIRouter(prefix="/v4/arc_remesas_documentos", tags=["archivo"])


@arc_remesas_documentos.get("", response_model=CustomPage[ArcRemesaDocumentoOut])
async def listado_arc_remesas_documentos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    arc_documento_id: int = None,
    arc_remesa_id: int = None,
):
    """Listado de documentos de remesas"""
    if current_user.permissions.get("ARC REMESAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_arc_remesas_documentos(
            database=database,
            arc_documento_id=arc_documento_id,
            arc_remesa_id=arc_remesa_id,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@arc_remesas_documentos.get("/{arc_remesa_documento_id}", response_model=OneArcRemesaDocumentoOut)
async def detalle_arc_remesa_documento(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    arc_remesa_documento_id: int,
):
    """Detalle de una documento de remesa a partir de su id"""
    if current_user.permissions.get("ARC REMESAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        arc_remesa_documento = get_arc_remesa_documento(database, arc_remesa_documento_id)
    except MyAnyError as error:
        return OneArcRemesaDocumentoOut(success=False, message=str(error))
    return OneArcRemesaDocumentoOut.from_orm(arc_remesa_documento)
