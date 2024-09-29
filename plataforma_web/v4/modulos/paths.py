"""
Modulos v4, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList
from plataforma_web.core.permisos.models import Permiso
from plataforma_web.v4.modulos.crud import get_modulo, get_modulos
from plataforma_web.v4.modulos.schemas import ItemModuloOut, OneModuloOut
from plataforma_web.v4.usuarios.authentications import AuthenticatedUser, get_current_active_user

modulos = APIRouter(prefix="/v4/modulos", tags=["usuarios"])


@modulos.get("/{modulo_id}", response_model=OneModuloOut)
async def detalle_modulo(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    modulo_id: int,
):
    """Detalle de un modulo a partir de su id"""
    if current_user.permissions.get("MODULOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        modulo = get_modulo(database, modulo_id)
    except MyAnyError as error:
        return OneModuloOut(success=False, message=str(error))
    return OneModuloOut.model_validate(modulo)


@modulos.get("", response_model=CustomList[ItemModuloOut])
async def listado_modulos(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de modulos"""
    if current_user.permissions.get("MODULOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_modulos(database)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)
