"""
Inventarios Equipos v3, CRUD (create, read, update, and delete)
"""
from datetime import date, datetime
from typing import Any

from sqlalchemy.orm import Session
import pytz

from lib.exceptions import MyIsDeletedError, MyNotExistsError
from lib.safe_string import safe_string

from ...core.inv_equipos.models import InvEquipo
from ...core.inv_custodias.models import InvCustodia
from ...core.usuarios.models import Usuario
from ..inv_custodias.crud import get_inv_custodia
from ..inv_modelos.crud import get_inv_modelo
from ..inv_redes.crud import get_inv_red
from ..oficinas.crud import get_oficina, get_oficina_with_clave


def get_inv_equipos(
    db: Session,
    creado: date = None,
    creado_desde: date = None,
    creado_hasta: date = None,
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
    servidor_huso_horario = pytz.utc
    consulta = db.query(InvEquipo)
    if creado is not None:
        desde_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=0, minute=0, second=0).astimezone(servidor_huso_horario)
        hasta_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=23, minute=59, second=59).astimezone(servidor_huso_horario)
        consulta = consulta.filter(InvEquipo.creado >= desde_dt).filter(InvEquipo.creado <= hasta_dt)
    if creado is None and creado_desde is not None:
        desde_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=0, minute=0, second=0).astimezone(servidor_huso_horario)
        consulta = consulta.filter(InvEquipo.creado >= desde_dt)
    if creado is None and creado_hasta is not None:
        hasta_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=23, minute=59, second=59).astimezone(servidor_huso_horario)
        consulta = consulta.filter(InvEquipo.creado <= hasta_dt)
    if fecha_fabricacion_desde is not None:
        consulta = consulta.filter(InvEquipo.fecha_fabricacion >= fecha_fabricacion_desde)
    if fecha_fabricacion_hasta is not None:
        consulta = consulta.filter(InvEquipo.fecha_fabricacion <= fecha_fabricacion_hasta)
    if inv_custodia_id is not None:
        inv_custodia = get_inv_custodia(db, inv_custodia_id)
        consulta = consulta.filter(InvEquipo.inv_custodia == inv_custodia)
    if inv_modelo_id is not None:
        inv_modelo = get_inv_modelo(db, inv_modelo_id)
        consulta = consulta.filter(InvEquipo.inv_modelo == inv_modelo)
    if inv_red_id is not None:
        inv_red = get_inv_red(db, inv_red_id)
        consulta = consulta.filter(InvEquipo.inv_red == inv_red)
    if oficina_id is not None:
        oficina = get_oficina(db, oficina_id)
        consulta = consulta.join(InvCustodia, Usuario)
        consulta = consulta.filter(Usuario.oficina == oficina)
    elif oficina_clave is not None:
        oficina = get_oficina_with_clave(db, oficina_clave)
        consulta = consulta.join(InvCustodia, Usuario)
        consulta = consulta.filter(Usuario.oficina == oficina)
    if tipo is not None:
        tipo = safe_string(tipo)
        if tipo in InvEquipo.TIPOS:
            consulta = consulta.filter(InvEquipo.tipo == tipo)
    return consulta.filter_by(estatus="A").order_by(InvEquipo.id)


def get_inv_equipo(db: Session, inv_equipo_id: int) -> InvEquipo:
    """Consultar un equipo por su id"""
    inv_equipo = db.query(InvEquipo).get(inv_equipo_id)
    if inv_equipo is None:
        raise MyNotExistsError("No existe ese equipo")
    if inv_equipo.estatus != "A":
        raise MyIsDeletedError("No es activo ese equipo, está eliminado")
    return inv_equipo
