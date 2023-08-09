"""
Inventarios Redes v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_inv_red, get_inv_redes
from .schemas import InvRedOut, OneInvRedOut

inv_redes = APIRouter(prefix="/v4/inv_redes", tags=["inventarios"])


@inv_redes.get("", response_model=CustomPage[InvRedOut])
async def paginado_inv_redes(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de redes"""
    if current_user.permissions.get("INV REDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_redes(database)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@inv_redes.get("/{inv_red_id}", response_model=OneInvRedOut)
async def detalle_inv_red(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    inv_red_id: int,
):
    """Detalle de una red a partir de su id"""
    if current_user.permissions.get("INV REDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_red = get_inv_red(database, inv_red_id)
    except MyAnyError as error:
        return OneInvRedOut(success=False, message=str(error))
    return OneInvRedOut.model_validate(inv_red)
