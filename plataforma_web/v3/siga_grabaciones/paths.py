"""
SIGA Grabaciones v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_siga_grabaciones, get_siga_grabacion, create_siga_gabacion
from .schemas import SIGAGrabacionIn, SIGAGrabacionOut, OneSIGAGrabacionOut

siga_grabaciones = APIRouter(prefix="/v3/siga_grabaciones", tags=["siga"])


@siga_grabaciones.get("", response_model=CustomPage[SIGAGrabacionOut])
async def listado_siga_grabaciones(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    siga_sala_id: int = None,
    siga_sala_clave: str = None,
):
    """Listado de grabaciones"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_siga_grabaciones(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            siga_sala_id=siga_sala_id,
            siga_sala_clave=siga_sala_clave,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@siga_grabaciones.get("/{siga_grabacion_id}", response_model=OneSIGAGrabacionOut)
async def detalle_siga_grabacion(
    current_user: CurrentUser,
    db: DatabaseSession,
    siga_grabacion_id: int,
):
    """Detalle de una grabacion a partir de su id"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_grabacion = get_siga_grabacion(db, siga_grabacion_id)
    except MyAnyError as error:
        return OneSIGAGrabacionOut(success=False, message=str(error))
    return OneSIGAGrabacionOut.from_orm(siga_grabacion)


@siga_grabaciones.post("", response_model=OneSIGAGrabacionOut)
async def crear_siga_grabacion(
    current_user: CurrentUser,
    db: DatabaseSession,
    siga_grabacion: SIGAGrabacionIn,
):
    """Crear una grabacion"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.CREAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_grabacion = create_siga_gabacion(db, siga_grabacion)
    except MyAnyError as error:
        return OneSIGAGrabacionOut(success=False, message=str(error))
    respuesta = OneSIGAGrabacionOut.from_orm(siga_grabacion)
    respuesta.message = "SIGA grabacion creada correctamente"
    return respuesta
