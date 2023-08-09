"""
Inventarios Modelos v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_inv_modelo, get_inv_modelos
from .schemas import InvModeloOut, OneInvModeloOut

inv_modelos = APIRouter(prefix="/v4/inv_modelos", tags=["inventarios"])


@inv_modelos.get("", response_model=CustomPage[InvModeloOut])
async def paginado_inv_modelos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    inv_marca_id: int = None,
):
    """Paginado de modelos"""
    if current_user.permissions.get("INV MODELOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_modelos(
            database=database,
            inv_marca_id=inv_marca_id,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@inv_modelos.get("/{inv_modelo_id}", response_model=OneInvModeloOut)
async def detalle_inv_modelo(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    inv_modelo_id: int,
):
    """Detalle de una modelo a partir de su id"""
    if current_user.permissions.get("INV MODELOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_modelo = get_inv_modelo(database, inv_modelo_id)
    except MyAnyError as error:
        return OneInvModeloOut(success=False, message=str(error))
    return OneInvModeloOut.model_validate(inv_modelo)
