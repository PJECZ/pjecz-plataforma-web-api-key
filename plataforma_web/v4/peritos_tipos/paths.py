"""
Tipos de Peritos v4, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList
from plataforma_web.core.permisos.models import Permiso
from plataforma_web.v4.peritos_tipos.crud import get_perito_tipo, get_peritos_tipos
from plataforma_web.v4.peritos_tipos.schemas import ItemPeritoTipoOut, OnePeritoTipoOut
from plataforma_web.v4.usuarios.authentications import AuthenticatedUser, get_current_active_user

peritos_tipos = APIRouter(prefix="/v4/peritos_tipos", tags=["peritos"])


@peritos_tipos.get("/{perito_tipo_id}", response_model=OnePeritoTipoOut)
async def detalle_perito_tipo(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    perito_tipo_id: int,
):
    """Detalle de un tipo de perito a partir de su id"""
    if current_user.permissions.get("PERITOS TIPOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        perito_tipo = get_perito_tipo(database, perito_tipo_id)
    except MyAnyError as error:
        return OnePeritoTipoOut(success=False, message=str(error))
    return OnePeritoTipoOut.model_validate(perito_tipo)


@peritos_tipos.get("", response_model=CustomList[ItemPeritoTipoOut])
async def listado_peritos_tipos(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de tipos de peritos"""
    if current_user.permissions.get("PERITOS TIPOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_peritos_tipos(database)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)
