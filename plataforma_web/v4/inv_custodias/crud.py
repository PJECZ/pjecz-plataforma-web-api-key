"""
Inventarios Custodias v3, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.inv_custodias.models import InvCustodia
from ...core.oficinas.models import Oficina
from ...core.usuarios.models import Usuario
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..oficinas.crud import get_oficina, get_oficina_with_clave
from ..usuarios.crud import get_usuario, get_usuario_with_email


def get_inv_custodias(
    database: Session,
    distrito_id: int = None,
    distrito_clave: str = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
    oficina_id: int = None,
    oficina_clave: str = None,
    usuario_id: int = None,
    usuario_email: str = None,
) -> Any:
    """Consultar los custodias activos"""
    consulta = database.query(InvCustodia)
    if fecha_desde is not None:
        consulta = consulta.filter(InvCustodia.fecha >= fecha_desde)
    if fecha_hasta is not None:
        consulta = consulta.filter(InvCustodia.fecha <= fecha_hasta)
    if oficina_id is not None:
        oficina = get_oficina(database, oficina_id)
        consulta = consulta.join(Usuario)
        consulta = consulta.filter(Usuario.oficina == oficina)
    elif oficina_clave is not None:
        oficina = get_oficina_with_clave(database, oficina_clave)
        consulta = consulta.join(Usuario)
        consulta = consulta.filter(Usuario.oficina == oficina)
    elif distrito_id is not None:
        distrito = get_distrito(database, distrito_id)
        consulta = consulta.join(Usuario)
        consulta = consulta.join(Oficina)
        consulta = consulta.filter(Oficina.distrito == distrito)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(database, distrito_clave)
        consulta = consulta.join(Usuario)
        consulta = consulta.join(Oficina)
        consulta = consulta.filter(Oficina.distrito == distrito)
    if usuario_id is not None:
        usuario = get_usuario(database, usuario_id=usuario_id)
        consulta = consulta.filter(InvCustodia.usuario == usuario)
    elif usuario_email is not None:
        usuario = get_usuario_with_email(database, usuario_email)
        consulta = consulta.filter(InvCustodia.usuario == usuario)
    return consulta.filter_by(estatus="A").order_by(InvCustodia.id.desc())


def get_inv_custodia(database: Session, inv_custodia_id: int) -> InvCustodia:
    """Consultar un custodia por su id"""
    inv_custodia = database.query(InvCustodia).get(inv_custodia_id)
    if inv_custodia is None:
        raise MyNotExistsError("No existe ese custodia")
    if inv_custodia.estatus != "A":
        raise MyIsDeletedError("No es activo ese custodia, está eliminado")
    return inv_custodia
