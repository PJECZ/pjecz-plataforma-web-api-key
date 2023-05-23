"""
Inventarios Marcas v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_inv_marcas, get_inv_marca
from .schemas import InvMarcaOut, OneInvMarcaOut

inv_marcas = APIRouter(prefix="/v3/inv_marcas", tags=["inventarios"])


@inv_marcas.get("", response_model=CustomPage[InvMarcaOut])
async def listado_inv_marcas(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de marcas"""
    if current_user.permissions.get("INV MARCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_marcas(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@inv_marcas.get("/{inv_marca_id}", response_model=OneInvMarcaOut)
async def detalle_inv_marca(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_marca_id: int,
):
    """Detalle de una marca a partir de su id"""
    if current_user.permissions.get("INV MARCAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_marca = get_inv_marca(db=db, inv_marca_id=inv_marca_id)
    except MyAnyError as error:
        return OneInvMarcaOut(success=False, message=str(error))
    return OneInvMarcaOut.from_orm(inv_marca)
