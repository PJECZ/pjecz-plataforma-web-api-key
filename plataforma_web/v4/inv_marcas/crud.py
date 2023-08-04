"""
Inventarios Marcas v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.inv_marcas.models import InvMarca


def get_inv_marcas(database: Session) -> Any:
    """Consultar los marcas activos"""
    return database.query(InvMarca).filter_by(estatus="A").order_by(InvMarca.nombre)


def get_inv_marca(database: Session, inv_marca_id: int) -> InvMarca:
    """Consultar un marca por su id"""
    inv_marca = database.query(InvMarca).get(inv_marca_id)
    if inv_marca is None:
        raise MyNotExistsError("No existe ese marca")
    if inv_marca.estatus != "A":
        raise MyIsDeletedError("No es activo ese marca, está eliminado")
    return inv_marca
