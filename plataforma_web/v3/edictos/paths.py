"""
Edictos v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.edictos.models import Edicto
from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import create_edicto, delete_edicto, get_edicto, get_edictos, update_edicto
from .schemas import EdictoIn, EdictoOut, OneEdictoOut

edictos = APIRouter(prefix="/v3/edictos", tags=["edictos"])


@edictos.get("", response_model=CustomPage[EdictoOut])
async def listado_edictos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    expediente: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
):
    """Listado de edictos"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_edictos(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            anio=anio,
            expediente=expediente,
            fecha=fecha,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@edictos.get("/{edicto_id}", response_model=OneEdictoOut)
async def detalle_edicto(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    edicto_id: int,
):
    """Detalle de un edicto a partir de su id"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        edicto = get_edicto(db, edicto_id)
    except MyAnyError as error:
        return OneEdictoOut(success=False, message=str(error))
    return OneEdictoOut.from_orm(edicto)


@edictos.post("", response_model=OneEdictoOut)
async def crear_edicto(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    edicto_in: EdictoIn,
):
    """Crear un edicto"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.CREAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        edicto = create_edicto(db, Edicto(**edicto_in.dict()))
    except MyAnyError as error:
        return OneEdictoOut(success=False, message=str(error))
    respuesta = OneEdictoOut.from_orm(edicto)
    respuesta.message = "Edicto creado correctamente"
    return respuesta


@edictos.put("/{edicto_id}", response_model=OneEdictoOut)
async def modificar_edicto(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    edicto_id: int,
    edicto_in: EdictoIn,
):
    """Modificar un edicto"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.MODIFICAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        edicto = update_edicto(db, edicto_id, edicto_in=Edicto(**edicto_in.dict()))
    except MyAnyError as error:
        return OneEdictoOut(success=False, message=str(error))
    respuesta = OneEdictoOut.from_orm(edicto)
    respuesta.message = "Edicto actualizado correctamente"
    return respuesta


@edictos.delete("/{edicto_id}", response_model=OneEdictoOut)
async def borrar_edicto(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    edicto_id: int,
):
    """Borrar un edicto"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.BORRAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        edicto = delete_edicto(db, edicto_id)
    except MyAnyError as error:
        return OneEdictoOut(success=False, message=str(error))
    respuesta = OneEdictoOut.from_orm(edicto)
    respuesta.message = "Edicto borrado correctamente"
    return respuesta
