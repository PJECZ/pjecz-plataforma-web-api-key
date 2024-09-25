"""
Epocas v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_epoca, get_epocas
from .schemas import EpocaListOut, EpocaOut, OneEpocaOut

epocas = APIRouter(prefix="/v4/epocas", tags=["tesis jurisprudencias"])


@epocas.get("", response_model=CustomPage[EpocaOut])
async def paginado_epocas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de epocas"""
    if current_user.permissions.get("EPOCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_epocas(database)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@epocas.get("/listado", response_model=CustomList[EpocaListOut])
async def listado_epocas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de epocas"""
    if current_user.permissions.get("EPOCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_epocas(database)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)


@epocas.get("/{epoca_id}", response_model=OneEpocaOut)
async def detalle_epoca(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    epoca_id: int,
):
    """Detalle de una epoca a partir de su id"""
    if current_user.permissions.get("EPOCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        epoca = get_epoca(database, epoca_id)
    except MyAnyError as error:
        return OneEpocaOut(success=False, message=str(error))
    return OneEpocaOut.model_validate(epoca)
