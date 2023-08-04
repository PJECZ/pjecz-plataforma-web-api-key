"""
Inventarios Redes v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.inv_redes.models import InvRed


def get_inv_redes(database: Session) -> Any:
    """Consultar las redes activas"""
    return database.query(InvRed).filter_by(estatus="A").order_by(InvRed.nombre)


def get_inv_red(database: Session, inv_red_id: int) -> InvRed:
    """Consultar una red por su id"""
    inv_red = database.query(InvRed).get(inv_red_id)
    if inv_red is None:
        raise MyNotExistsError("No existe ese red")
    if inv_red.estatus != "A":
        raise MyIsDeletedError("No es activo ese red, está eliminado")
    return inv_red
