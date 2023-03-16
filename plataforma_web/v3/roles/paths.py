"""
Roles v3, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import get_current_active_user
from ..usuarios.schemas import UsuarioInDB

from .crud import get_roles, get_rol_by_nombre
from .schemas import RolOut, OneRolOut

roles = APIRouter(prefix="/v3/roles", tags=["usuarios"])


@roles.get("", response_model=CustomPage[RolOut])
async def listado_roles(
    current_user: UsuarioInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Listado de roles"""
    if current_user.permissions.get("ROLES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_roles(db=db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@roles.get("/{nombre}", response_model=OneRolOut)
async def detalle_rol(
    nombre: str,
    current_user: UsuarioInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de una roles a partir de su id"""
    if current_user.permissions.get("ROLES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        rol = get_rol_by_nombre(db=db, nombre=nombre)
    except MyAnyError as error:
        return OneRolOut(success=False, message=str(error))
    return OneRolOut.from_orm(rol)
