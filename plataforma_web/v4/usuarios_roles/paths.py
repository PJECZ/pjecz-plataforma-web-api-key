"""
Usuarios-Roles v4, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage
from plataforma_web.core.permisos.models import Permiso
from plataforma_web.v4.usuarios.authentications import AuthenticatedUser, get_current_active_user
from plataforma_web.v4.usuarios_roles.crud import get_usuario_rol, get_usuarios_roles
from plataforma_web.v4.usuarios_roles.schemas import ItemUsuarioRolOut, OneUsuarioRolOut

usuarios_roles = APIRouter(prefix="/v4/usuarios_roles", tags=["usuarios"])


@usuarios_roles.get("/{usuario_rol_id}", response_model=OneUsuarioRolOut)
async def detalle_usuario_rol(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    usuario_rol_id: int,
):
    """Detalle de una usuarios-roles a partir de su id"""
    if current_user.permissions.get("USUARIOS ROLES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        usuario_rol = get_usuario_rol(database, usuario_rol_id)
    except MyAnyError as error:
        return OneUsuarioRolOut(success=False, message=str(error))
    return OneUsuarioRolOut.model_validate(usuario_rol)


@usuarios_roles.get("", response_model=CustomPage[ItemUsuarioRolOut])
async def paginado_usuarios_roles(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    rol_id: int = None,
    rol_nombre: str = None,
    usuario_id: int = None,
    usuario_email: str = None,
):
    """Paginado de usuarios-roles"""
    if current_user.permissions.get("USUARIOS ROLES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_usuarios_roles(
            database=database,
            rol_id=rol_id,
            rol_nombre=rol_nombre,
            usuario_id=usuario_id,
            usuario_email=usuario_email,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)
