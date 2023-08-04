"""
Inventarios Componentes v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError
from lib.safe_string import safe_string

from ...core.inv_componentes.models import InvComponente
from ..inv_categorias.crud import get_inv_categoria
from ..inv_equipos.crud import get_inv_equipo


def get_inv_componentes(
    database: Session,
    inv_categoria_id: int = None,
    inv_equipo_id: int = None,
    generacion: str = None,
) -> Any:
    """Consultar los componentes activos"""
    consulta = database.query(InvComponente)
    if inv_categoria_id is not None:
        inv_categoria = get_inv_categoria(database, inv_categoria_id=inv_categoria_id)
        consulta = consulta.filter(InvComponente.inv_categoria == inv_categoria)
    if inv_equipo_id is not None:
        inv_equipo = get_inv_equipo(database, inv_equipo_id=inv_equipo_id)
        consulta = consulta.filter(InvComponente.inv_equipo == inv_equipo)
    if generacion is not None:
        generacion = safe_string(generacion)
        if generacion != "":
            consulta = consulta.filter_by(generacion=generacion)
    return consulta.filter_by(estatus="A").order_by(InvComponente.id.desc())


def get_inv_componente(database: Session, inv_componente_id: int) -> InvComponente:
    """Consultar un componente por su id"""
    inv_componente = database.query(InvComponente).get(inv_componente_id)
    if inv_componente is None:
        raise MyNotExistsError("No existe ese componente")
    if inv_componente.estatus != "A":
        raise MyIsDeletedError("No es activo ese componente, está eliminado")
    return inv_componente
