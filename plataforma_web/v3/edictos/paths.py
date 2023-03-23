"""
Edictos v3, rutas (paths)
"""
from datetime import date

from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_edictos, get_edicto
from .schemas import EdictoOut, OneEdictoOut

edictos = APIRouter(prefix="/v3/edictos", tags=["categoria"])


@edictos.get("", response_model=CustomPage[EdictoOut])
async def listado_edictos(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    anio: int = None,
    fecha: date = None,
):
    """Listado de edictos"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_edictos(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            anio=anio,
            fecha=fecha,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@edictos.get("/{edicto_id}", response_model=OneEdictoOut)
async def detalle_edicto(
    current_user: CurrentUser,
    db: DatabaseSession,
    edicto_id: int,
):
    """Detalle de un edicto a partir de su id"""
    if current_user.permissions.get("EDICTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        edicto = get_edicto(db=db, edicto_id=edicto_id)
    except MyAnyError as error:
        return OneEdictoOut(success=False, message=str(error))
    return OneEdictoOut.from_orm(edicto)
