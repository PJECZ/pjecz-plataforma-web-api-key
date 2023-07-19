"""
Boletines v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.boletines.models import Boletin
from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import create_boletin, delete_boletin, get_boletin, get_boletines, update_boletin
from .schemas import BoletinIn, BoletinOut, OneBoletinOut

boletines = APIRouter(prefix="/v3/boletines", tags=["boletines"])


@boletines.get("", response_model=CustomPage[BoletinOut])
async def listado_boletines(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    estado: str = None,
    envio_programado_desde: date = None,
    envio_programado_hasta: date = None,
):
    """Listado de boletines"""
    if current_user.permissions.get("BOLETINES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_boletines(
            db=db,
            estado=estado,
            envio_programado_desde=envio_programado_desde,
            envio_programado_hasta=envio_programado_hasta,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@boletines.get("/{boletin_id}", response_model=OneBoletinOut)
async def detalle_boletinget_boletin(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    boletin_id: int,
):
    """Detalle de una boletin a partir de su id"""
    if current_user.permissions.get("BOLETINES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        boletinget_boletin = get_boletin(db, boletin_id)
    except MyAnyError as error:
        return OneBoletinOut(success=False, message=str(error))
    return OneBoletinOut.from_orm(boletinget_boletin)


@boletines.post("", response_model=OneBoletinOut)
async def crear_boletin(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    boletin_in: BoletinIn,
):
    """Crear un boletin"""
    if current_user.permissions.get("BOLETINES", 0) < Permiso.CREAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        boletin = create_boletin(db, Boletin(**boletin_in.dict()))
    except MyAnyError as error:
        return OneBoletinOut(success=False, message=str(error))
    respuesta = OneBoletinOut.from_orm(boletin)
    respuesta.message = "Boletin creado correctamente"
    return respuesta


@boletines.put("/{boletin_id}", response_model=OneBoletinOut)
async def modificar_boletin(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    boletin_id: int,
    boletin_in: BoletinIn,
):
    """Modificar un boletin"""
    if current_user.permissions.get("BOLETINES", 0) < Permiso.MODIFICAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        boletin = update_boletin(db, boletin_id, boletin_in)
    except MyAnyError as error:
        return OneBoletinOut(success=False, message=str(error))
    respuesta = OneBoletinOut.from_orm(boletin)
    respuesta.message = "Boletin modificado correctamente"
    return respuesta


@boletines.delete("/{boletin_id}", response_model=OneBoletinOut)
async def borrar_boletin(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    boletin_id: int,
):
    """Borrar un boletin"""
    if current_user.permissions.get("BOLETINES", 0) < Permiso.BORRAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        boletin = delete_boletin(db, boletin_id)
    except MyAnyError as error:
        return OneBoletinOut(success=False, message=str(error))
    respuesta = OneBoletinOut.from_orm(boletin)
    respuesta.message = "Boletin borrado correctamente"
    return respuesta
