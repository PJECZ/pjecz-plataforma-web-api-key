"""
Epocas v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_epocas, get_epoca
from .schemas import EpocaOut, OneEpocaOut

epocas = APIRouter(prefix="/v3/epocas", tags=["tesis jurisprudencias"])


@epocas.get("", response_model=CustomPage[EpocaOut])
async def listado_epocas(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de epocas"""
    if current_user.permissions.get("EPOCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_epocas(db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@epocas.get("/{epoca_id}", response_model=OneEpocaOut)
async def detalle_epoca(
    current_user: CurrentUser,
    db: DatabaseSession,
    epoca_id: int,
):
    """Detalle de una epoca a partir de su id"""
    if current_user.permissions.get("EPOCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        epoca = get_epoca(db, epoca_id)
    except MyAnyError as error:
        return OneEpocaOut(success=False, message=str(error))
    return OneEpocaOut.from_orm(epoca)
