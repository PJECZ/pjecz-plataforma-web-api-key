"""
Inventarios Categorias v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.inv_categorias.models import InvCategoria


def get_inv_categorias(database: Session) -> Any:
    """Consultar los categorias activos"""
    return database.query(InvCategoria).filter_by(estatus="A").order_by(InvCategoria.nombre)


def get_inv_categoria(database: Session, inv_categoria_id: int) -> InvCategoria:
    """Consultar un categoria por su id"""
    inv_categoria = database.query(InvCategoria).get(inv_categoria_id)
    if inv_categoria is None:
        raise MyNotExistsError("No existe ese categoria")
    if inv_categoria.estatus != "A":
        raise MyIsDeletedError("No es activo ese categoria, está eliminado")
    return inv_categoria
