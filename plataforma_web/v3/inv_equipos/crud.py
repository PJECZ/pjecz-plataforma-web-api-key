"""
Inventarios Equipos v3, CRUD (create, read, update, and delete)
"""
from datetime import date, datetime
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError
from lib.safe_string import safe_string

from ...core.inv_equipos.models import InvEquipo
from ...core.inv_custodias.models import InvCustodia
from ...core.oficinas.models import Oficina
from ...core.usuarios.models import Usuario
from ..inv_custodias.crud import get_inv_custodia
from ..inv_modelos.crud import get_inv_modelo
from ..inv_redes.crud import get_inv_red
from ..oficinas.crud import get_oficina, get_oficina_from_clave


def get_inv_equipos(
    db: Session,
    creado: date = None,
    creado_desde: date = None,
    creado_hasta: date = None,
    estatus: str = None,
    fecha_fabricacion_desde: date = None,
    fecha_fabricacion_hasta: date = None,
    inv_custodia_id: int = None,
    inv_modelo_id: int = None,
    inv_red_id: int = None,
    oficina_id: int = None,
    oficina_clave: str = None,
    tipo: str = None,
) -> Any:
    """Consultar los equipos activos"""
    consulta = db.query(InvEquipo)
    return consulta.filter_by(estatus="A").order_by(InvEquipo.id)


def get_inv_equipo(db: Session, inv_equipo_id: int) -> InvEquipo:
    """Consultar un equipo por su id"""
    inv_equipo = db.query(InvEquipo).get(inv_equipo_id)
    if inv_equipo is None:
        raise MyNotExistsError("No existe ese equipo")
    if inv_equipo.estatus != "A":
        raise MyIsDeletedError("No es activo ese equipo, está eliminado")
    return inv_equipo
