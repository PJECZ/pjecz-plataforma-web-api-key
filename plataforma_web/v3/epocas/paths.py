"""
Epocas v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_epoca, get_epocas
from .schemas import EpocaOut, OneEpocaOut

epocas = APIRouter(prefix="/v3/epocas", tags=["tesis jurisprudencias"])


@epocas.get("", response_model=CustomPage[EpocaOut])
async def listado_epocas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Listado de epocas"""
    if current_user.permissions.get("EPOCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_epocas(db)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@epocas.get("/{epoca_id}", response_model=OneEpocaOut)
async def detalle_epoca(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
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
