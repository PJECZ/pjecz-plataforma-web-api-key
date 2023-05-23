"""
Inventarios Redes v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_inv_redes, get_inv_red
from .schemas import InvRedOut, OneInvRedOut

inv_redes = APIRouter(prefix="/v3/inv_redes", tags=["inventarios"])


@inv_redes.get("", response_model=CustomPage[InvRedOut])
async def listado_inv_redes(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de redes"""
    if current_user.permissions.get("INV REDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_redes(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@inv_redes.get("/{inv_red_id}", response_model=OneInvRedOut)
async def detalle_inv_red(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_red_id: int,
):
    """Detalle de una red a partir de su id"""
    if current_user.permissions.get("INV REDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_red = get_inv_red(db=db, inv_red_id=inv_red_id)
    except MyAnyError as error:
        return OneInvRedOut(success=False, message=str(error))
    return OneInvRedOut.from_orm(inv_red)
