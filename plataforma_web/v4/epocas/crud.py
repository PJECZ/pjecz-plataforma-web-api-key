"""
Epocas v3, CRUD (create, read, update, and delete)
"""

from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.epocas.models import Epoca


def get_epocas(database: Session) -> Any:
    """Consultar las epocas activas"""
    return database.query(Epoca).filter_by(estatus="A").order_by(Epoca.nombre)


def get_epoca(database: Session, epoca_id: int) -> Epoca:
    """Consultar una epoca por su id"""
    epoca = database.query(Epoca).get(epoca_id)
    if epoca is None:
        raise MyNotExistsError("No existe ese epoca")
    if epoca.estatus != "A":
        raise MyIsDeletedError("No es activo ese epoca, está eliminado")
    return epoca
