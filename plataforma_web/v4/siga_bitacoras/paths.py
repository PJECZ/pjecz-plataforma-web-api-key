"""
SIGA Bitacoras v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_siga_bitacora, get_siga_bitacoras
from .schemas import OneSIGABitacoraOut, SIGABitacoraOut

siga_bitacoras = APIRouter(prefix="/v4/siga_bitacoras", tags=["siga"])


@siga_bitacoras.get("", response_model=CustomPage[SIGABitacoraOut])
async def listado_siga_bitacoras(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    accion: str = None,
    estado: str = None,
    siga_sala_id: int = None,
    siga_sala_clave: str = None,
):
    """Listado de bitacoras"""
    if current_user.permissions.get("SIGA SALAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_siga_bitacoras(
            database=database,
            accion=accion,
            estado=estado,
            siga_sala_id=siga_sala_id,
            siga_sala_clave=siga_sala_clave,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@siga_bitacoras.get("/{siga_bitacora_id}", response_model=OneSIGABitacoraOut)
async def detalle_siga_bitacora(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    siga_bitacora_id: int,
):
    """Detalle de una bitacora a partir de su id"""
    if current_user.permissions.get("SIGA SALAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_bitacora = get_siga_bitacora(database, siga_bitacora_id)
    except MyAnyError as error:
        return OneSIGABitacoraOut(success=False, message=str(error))
    return OneSIGABitacoraOut.from_orm(siga_bitacora)
