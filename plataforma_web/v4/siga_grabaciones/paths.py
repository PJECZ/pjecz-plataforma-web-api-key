"""
SIGA Grabaciones v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ...core.siga_grabaciones.models import SIGAGrabacion
from ..autoridades.crud import get_autoridad_with_clave
from ..materias.crud import get_materia_with_clave
from ..siga_salas.crud import get_siga_sala_with_clave
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import create_siga_grabacion, get_siga_grabacion, get_siga_grabacion_with_archivo_nombre, get_siga_grabaciones
from .schemas import OneSIGAGrabacionOut, SIGAGrabacionIn, SIGAGrabacionOut

siga_grabaciones = APIRouter(prefix="/v4/siga_grabaciones", tags=["siga"])


@siga_grabaciones.get("/paginado", response_model=CustomPage[SIGAGrabacionOut])
async def listado_siga_grabaciones(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    materia_id: int = None,
    materia_clave: str = None,
    siga_sala_id: int = None,
    siga_sala_clave: str = None,
):
    """Listado de grabaciones"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_siga_grabaciones(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            materia_id=materia_id,
            materia_clave=materia_clave,
            siga_sala_id=siga_sala_id,
            siga_sala_clave=siga_sala_clave,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@siga_grabaciones.get("/archivo_nombre/{archivo_nombre}", response_model=OneSIGAGrabacionOut)
async def detalle_siga_grabacion_con_archivo_nombre(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    archivo_nombre: str,
):
    """Detalle de una grabacion a partir de su id"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_grabacion = get_siga_grabacion_with_archivo_nombre(database, archivo_nombre)
    except MyAnyError as error:
        return OneSIGAGrabacionOut(success=False, message=str(error))
    return OneSIGAGrabacionOut.from_orm(siga_grabacion)


@siga_grabaciones.get("/{siga_grabacion_id}", response_model=OneSIGAGrabacionOut)
async def detalle_siga_grabacion(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    siga_grabacion_id: int,
):
    """Detalle de una grabacion a partir de su id"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        siga_grabacion = get_siga_grabacion(database, siga_grabacion_id)
    except MyAnyError as error:
        return OneSIGAGrabacionOut(success=False, message=str(error))
    return OneSIGAGrabacionOut.from_orm(siga_grabacion)


@siga_grabaciones.post("", response_model=OneSIGAGrabacionOut)
async def crear_siga_grabacion(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    siga_grabacion_in: SIGAGrabacionIn,
):
    """Crear una grabacion"""
    if current_user.permissions.get("SIGA GRABACIONES", 0) < Permiso.CREAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        autoridad = get_autoridad_with_clave(database, siga_grabacion_in.autoridad_clave)
        materia = get_materia_with_clave(database, siga_grabacion_in.materia_clave)
        siga_sala = get_siga_sala_with_clave(database, siga_grabacion_in.siga_sala_clave)
        siga_grabacion = create_siga_grabacion(
            database,
            SIGAGrabacion(
                autoridad_id=autoridad.id,
                materia_id=materia.id,
                siga_sala_id=siga_sala.id,
                expediente=siga_grabacion_in.expediente,
                inicio=siga_grabacion_in.inicio,
                termino=siga_grabacion_in.termino,
                archivo_nombre=siga_grabacion_in.archivo_nombre,
                justicia_ruta=siga_grabacion_in.justicia_ruta,
                tamanio=siga_grabacion_in.tamanio,
                duracion=siga_grabacion_in.duracion,
                estado=siga_grabacion_in.estado,
            ),
        )
    except MyAnyError as error:
        return OneSIGAGrabacionOut(success=False, message=str(error))
    respuesta = OneSIGAGrabacionOut.from_orm(siga_grabacion)
    respuesta.message = "SIGA grabacion creada correctamente"
    return respuesta
