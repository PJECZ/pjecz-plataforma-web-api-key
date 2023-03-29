"""
REPSVM Agresores v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_repsvm_agresores, get_repsvm_agresor
from .schemas import RepsvmAgresorOut, OneRepsvmAgresorOut

repsvm_agresores = APIRouter(prefix="/v3/repsvm_agresores", tags=["repsvm agresores"])


@repsvm_agresores.get("", response_model=CustomPage[RepsvmAgresorOut])
async def listado_repsvm_agresores(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de agresores"""
    if current_user.permissions.get("REPSVM", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_repsvm_agresores(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@repsvm_agresores.get("/{repsvm_agresor_id}", response_model=OneRepsvmAgresorOut)
async def detalle_repsvm_agresor(
    current_user: CurrentUser,
    db: DatabaseSession,
    repsvm_agresor_id: int,
):
    """Detalle de una agresor a partir de su id"""
    if current_user.permissions.get("REPSVM", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        repsvm_agresor = get_repsvm_agresor(db=db, repsvm_agresor_id=repsvm_agresor_id)
    except MyAnyError as error:
        return OneRepsvmAgresorOut(success=False, message=str(error))
    return OneRepsvmAgresorOut.from_orm(repsvm_agresor)
