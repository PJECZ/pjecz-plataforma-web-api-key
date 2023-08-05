"""
SIGA Salas v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_siga_sala_with_clave, get_siga_salas
from .schemas import OneSIGASalaOut, SIGASalaOut

siga_salas = APIRouter(prefix="/v4/siga_salas", tags=["siga"])


@siga_salas.get("/paginado", response_model=CustomPage[SIGASalaOut])
async def listado_siga_salas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
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
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            domicilio_id=domicilio_id,
            estado=estado,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@siga_salas.get("/{siga_sala_clave}", response_model=OneSIGASalaOut)
async def detalle_siga_sala(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    siga_sala_clave: str,
):
    """Detalle de una sala a partir de su clave"""
    if current_user.permissions.get("SIGA SALAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_sala = get_siga_sala_with_clave(database, siga_sala_clave)
    except MyAnyError as error:
        return OneSIGASalaOut(success=False, message=str(error))
    return OneSIGASalaOut.from_orm(siga_sala)
