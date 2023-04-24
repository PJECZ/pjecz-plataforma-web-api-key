"""
Listas de Acuerdos v3, rutas (paths)
"""
from datetime import date

from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from ...core.listas_de_acuerdos.models import ListaDeAcuerdo
from .crud import get_listas_de_acuerdos, get_lista_de_acuerdo, create_lista_de_acuerdo, update_lista_de_acuerdo, delete_lista_de_acuerdo
from .schemas import ListaDeAcuerdoOut, OneListaDeAcuerdoOut

listas_de_acuerdos = APIRouter(prefix="/v3/listas_de_acuerdos", tags=["listas de acuerdos"])


@listas_de_acuerdos.get("", response_model=CustomPage[ListaDeAcuerdoOut])
async def listado_listas_de_acuerdos(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
):
    """Listado de listas de acuerdos"""
    if current_user.permissions.get("LISTAS DE ACUERDOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_listas_de_acuerdos(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            anio=anio,
            fecha=fecha,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@listas_de_acuerdos.get("/{lista_de_acuerdo_id}", response_model=OneListaDeAcuerdoOut)
async def detalle_lista_de_acuerdo(
    current_user: CurrentUser,
    db: DatabaseSession,
    lista_de_acuerdo_id: int,
):
    """Detalle de una lista de acuerdo a partir de su id"""
    if current_user.permissions.get("LISTAS DE ACUERDOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        lista_de_acuerdo = get_lista_de_acuerdo(db=db, lista_de_acuerdo_id=lista_de_acuerdo_id)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, message=str(error))
    return OneListaDeAcuerdoOut.from_orm(lista_de_acuerdo)


@listas_de_acuerdos.post("", response_model=OneListaDeAcuerdoOut)
async def crear_lista_de_acuerdo(
    current_user: CurrentUser,
    db: DatabaseSession,
    lista_de_acuerdo: ListaDeAcuerdoOut,
):
    """Crear una lista de acuerdo"""
    if current_user.permissions.get("LISTAS DE ACUERDOS", 0) < Permiso.CREAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        lista_de_acuerdo = create_lista_de_acuerdo(db=db, lista_de_acuerdo=lista_de_acuerdo)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, message=str(error))
    return OneListaDeAcuerdoOut.from_orm(lista_de_acuerdo)


@listas_de_acuerdos.put("/{lista_de_acuerdo_id}", response_model=OneListaDeAcuerdoOut)
async def actualizar_lista_de_acuerdo(
    current_user: CurrentUser,
    db: DatabaseSession,
    lista_de_acuerdo_id: int,
    lista_de_acuerdo: ListaDeAcuerdoOut,
):
    """Actualizar una lista de acuerdo"""
    if current_user.permissions.get("LISTAS DE ACUERDOS", 0) < Permiso.MODIFICAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        lista_de_acuerdo = update_lista_de_acuerdo(db=db, lista_de_acuerdo_id=lista_de_acuerdo_id, lista_de_acuerdo=lista_de_acuerdo)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, message=str(error))
    return OneListaDeAcuerdoOut.from_orm(lista_de_acuerdo)


@listas_de_acuerdos.delete("/{lista_de_acuerdo_id}", response_model=OneListaDeAcuerdoOut)
async def borrar_lista_de_acuerdo(
    current_user: CurrentUser,
    db: DatabaseSession,
    lista_de_acuerdo_id: int,
):
    """Borrar una lista de acuerdo"""
    if current_user.permissions.get("LISTAS DE ACUERDOS", 0) < Permiso.MODIFICAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        lista_de_acuerdo = delete_lista_de_acuerdo(db=db, lista_de_acuerdo_id=lista_de_acuerdo_id)
    except MyAnyError as error:
        return OneListaDeAcuerdoOut(success=False, message=str(error))
    return OneListaDeAcuerdoOut.from_orm(lista_de_acuerdo)
