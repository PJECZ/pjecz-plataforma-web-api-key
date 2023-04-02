"""
Peritos v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_peritos, get_perito
from .schemas import PeritoOut, OnePeritoOut

peritos = APIRouter(prefix="/v3/peritos", tags=["peritos"])


@peritos.get("", response_model=CustomPage[PeritoOut])
async def listado_peritos(
    current_user: CurrentUser,
    db: DatabaseSession,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    perito_tipo_id: int = None,
):
    """Listado de peritos"""
    if current_user.permissions.get("PERITOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_peritos(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            perito_tipo_id=perito_tipo_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@peritos.get("/{perito_id}", response_model=OnePeritoOut)
async def detalle_perito(
    current_user: CurrentUser,
    db: DatabaseSession,
    perito_id: int,
):
    """Detalle de un perito a partir de su id"""
    if current_user.permissions.get("PERITOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        perito = get_perito(db=db, perito_id=perito_id)
    except MyAnyError as error:
        return OnePeritoOut(success=False, message=str(error))
    return OnePeritoOut.from_orm(perito)
