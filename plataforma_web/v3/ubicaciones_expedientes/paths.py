"""
Ubicaciones de Expedientes v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_ubicaciones_expedientes, get_ubicacion_expediente
from .schemas import UbicacionExpedienteOut, OneUbicacionExpedienteOut

ubicaciones_expedientes = APIRouter(prefix="/v3/ubicaciones_expedientes", tags=["ubicaciones de expedientes"])


@ubicaciones_expedientes.get("", response_model=CustomPage[UbicacionExpedienteOut])
async def listado_ubicaciones_expedientes(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
):
    """Listado de ubicaciones de expedientes"""
    if current_user.permissions.get("UBICACIONES EXPEDIENTES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_ubicaciones_expedientes(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            expediente=expediente,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@ubicaciones_expedientes.get("/{ubicacion_expediente_id}", response_model=OneUbicacionExpedienteOut)
async def detalle_ubicacion_expediente(
    current_user: CurrentUser,
    db: DatabaseSession,
    ubicacion_expediente_id: int,
):
    """Detalle de una ubicacion de expediente a partir de su id"""
    if current_user.permissions.get("UBICACIONES EXPEDIENTES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        ubicacion_expediente = get_ubicacion_expediente(db, ubicacion_expediente_id)
    except MyAnyError as error:
        return OneUbicacionExpedienteOut(success=False, message=str(error))
    return OneUbicacionExpedienteOut.from_orm(ubicacion_expediente)
