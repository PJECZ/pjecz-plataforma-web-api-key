"""
SIGA Salas v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_siga_salas, get_siga_sala_with_clave
from .schemas import SIGASalaOut, OneSIGASalaOut

siga_salas = APIRouter(prefix="/v3/siga_salas", tags=["siga"])


@siga_salas.get("", response_model=CustomPage[SIGASalaOut])
async def listado_siga_salas(
    current_user: CurrentUser,
    db: DatabaseSession,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
    estado: str = None,
):
    """Listado de salas"""
    if current_user.permissions.get("SIGA SALAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_siga_salas(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            domicilio_id=domicilio_id,
            estado=estado,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@siga_salas.get("/{siga_sala_clave}", response_model=OneSIGASalaOut)
async def detalle_siga_sala(
    current_user: CurrentUser,
    db: DatabaseSession,
    siga_sala_clave: str,
):
    """Detalle de una sala a partir de su clave"""
    if current_user.permissions.get("SIGA SALAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_sala = get_siga_sala_with_clave(db, siga_sala_clave)
    except MyAnyError as error:
        return OneSIGASalaOut(success=False, message=str(error))
    return OneSIGASalaOut.from_orm(siga_sala)
