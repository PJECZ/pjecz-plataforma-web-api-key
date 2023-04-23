"""
REDAM (Registro Estatal de Deudores Alimentarios Morosos) v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_redams, get_redam
from .schemas import RedamOut, OneRedamOut

redam = APIRouter(prefix="/v3/redam", tags=["redam"])


@redam.get("", response_model=CustomPage[RedamOut])
async def listado_redams(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    nombre: str = None,
    expediente: str = None,
):
    """Listado de Deudores Alimentarios Morosos"""
    if current_user.permissions.get("REDAMS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_redams(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            nombre=nombre,
            expediente=expediente,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@redam.get("/{redam_id}", response_model=OneRedamOut)
async def detalle_redam(
    current_user: CurrentUser,
    db: DatabaseSession,
    redam_id: int,
):
    """Detalle de un Deudor Alimentario Moroso a partir de su id"""
    if current_user.permissions.get("REDAMS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        deudor = get_redam(db=db, redam_id=redam_id)
    except MyAnyError as error:
        return OneRedamOut(success=False, message=str(error))
    return OneRedamOut.from_orm(deudor)
