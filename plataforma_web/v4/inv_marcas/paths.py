"""
Inventarios Marcas v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_inv_marca, get_inv_marcas
from .schemas import InvMarcaOut, OneInvMarcaOut

inv_marcas = APIRouter(prefix="/v4/inv_marcas", tags=["inventarios"])


@inv_marcas.get("", response_model=CustomPage[InvMarcaOut])
async def listado_inv_marcas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de marcas"""
    if current_user.permissions.get("INV MARCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_marcas(database)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@inv_marcas.get("/{inv_marca_id}", response_model=OneInvMarcaOut)
async def detalle_inv_marca(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    inv_marca_id: int,
):
    """Detalle de una marca a partir de su id"""
    if current_user.permissions.get("INV MARCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_marca = get_inv_marca(database, inv_marca_id)
    except MyAnyError as error:
        return OneInvMarcaOut(success=False, message=str(error))
    return OneInvMarcaOut.from_orm(inv_marca)
