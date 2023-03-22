"""
Materias v3, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.materias.models import Materia


def get_materias(db: Session) -> Any:
    """Consultar las materias activas"""
    return db.query(Materia).filter_by(estatus="A").order_by(Materia.nombre)


def get_materia(db: Session, materia_id: int) -> Materia:
    """Consultar una materia por su id"""
    materia = db.query(Materia).get(materia_id)
    if materia is None:
        raise MyNotExistsError("No existe ese materia")
    if materia.estatus != "A":
        raise MyIsDeletedError("No es activo ese materia, está eliminado")
    return materia
