"""
Archivo - Juzgados Extintos v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.arc_juzgados_extintos.models import ArcJuzgadoExtinto


def get_arc_juzgados_extintos(database: Session) -> Any:
    """Consultar los juzgados extintos activos"""
    return database.query(ArcJuzgadoExtinto).filter_by(estatus="A").order_by(ArcJuzgadoExtinto.id)


def get_arc_juzgado_extinto(database: Session, arc_juzgado_extinto_id: int) -> ArcJuzgadoExtinto:
    """Consultar un juzgado extinto por su id"""
    arc_juzgado_extinto = database.query(ArcJuzgadoExtinto).get(arc_juzgado_extinto_id)
    if arc_juzgado_extinto is None:
        raise MyNotExistsError("No existe ese juzgado extinto")
    if arc_juzgado_extinto.estatus != "A":
        raise MyIsDeletedError("No es activo ese juzgado extinto, está eliminado")
    return arc_juzgado_extinto
