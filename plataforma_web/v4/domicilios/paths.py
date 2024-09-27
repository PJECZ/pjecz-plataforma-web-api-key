"""
Domicilios v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList
from plataforma_web.core.permisos.models import Permiso
from plataforma_web.v4.domicilios.crud import get_domicilio, get_domicilios
from plataforma_web.v4.domicilios.schemas import ItemDomicilioOut, OneDomicilioOut
from plataforma_web.v4.usuarios.authentications import AuthenticatedUser, get_current_active_user

domicilios = APIRouter(prefix="/v4/domicilios", tags=["oficinas"])


@domicilios.get("", response_model=CustomList[ItemDomicilioOut])
async def listado_domicilios(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    distrito_id: int = None,
    distrito_clave: str = None,
):
    """Listado de domicilios"""
    if current_user.permissions.get("DOMICILIOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_domicilios(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
        )
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)


@domicilios.get("/{domicilio_id}", response_model=OneDomicilioOut)
async def detalle_domicilio(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    domicilio_id: int,
):
    """Detalle de una domicilio a partir de su id"""
    if current_user.permissions.get("DOMICILIOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        domicilio = get_domicilio(database, domicilio_id)
    except MyAnyError as error:
        return OneDomicilioOut(success=False, message=str(error))
    return OneDomicilioOut.model_validate(domicilio)
