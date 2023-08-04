"""
Roles v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.roles.models import Rol


def get_roles(database: Session) -> Any:
    """Consultar los roles activos"""
    return database.query(Rol).filter_by(estatus="A").order_by(Rol.nombre)


def get_rol(database: Session, rol_id: int) -> Rol:
    """Consultar un rol por su id"""
    rol = database.query(Rol).get(rol_id)
    if rol is None:
        raise MyNotExistsError("No existe ese rol")
    if rol.estatus != "A":
        raise MyIsDeletedError("No es activo ese rol, está eliminado")
    return rol
