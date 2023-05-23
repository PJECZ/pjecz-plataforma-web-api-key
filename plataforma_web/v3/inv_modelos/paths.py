"""
Inventarios Modelos v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_inv_modelos, get_inv_modelo
from .schemas import InvModeloOut, OneInvModeloOut

inv_modelos = APIRouter(prefix="/v3/inv_modelos", tags=["inventarios"])


@inv_modelos.get("", response_model=CustomPage[InvModeloOut])
async def listado_inv_modelos(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_marca_id: int = None,
):
    """Listado de modelos"""
    if current_user.permissions.get("INV MODELOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_modelos(
            db=db,
            inv_marca_id=inv_marca_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@inv_modelos.get("/{inv_modelo_id}", response_model=OneInvModeloOut)
async def detalle_inv_modelo(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_modelo_id: int,
):
    """Detalle de una modelo a partir de su id"""
    if current_user.permissions.get("INV MODELOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_modelo = get_inv_modelo(db=db, inv_modelo_id=inv_modelo_id)
    except MyAnyError as error:
        return OneInvModeloOut(success=False, message=str(error))
    return OneInvModeloOut.from_orm(inv_modelo)
