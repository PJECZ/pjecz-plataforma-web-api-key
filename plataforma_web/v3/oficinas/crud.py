"""
Oficinas v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.oficinas.models import Oficina
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..domicilios.crud import get_domicilio


def get_oficinas(
    db: Session,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
    es_jurisdiccional: bool = None,
) -> Any:
    """Consultar las oficinas activas"""
    consulta = db.query(Oficina)
    if distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(db, distrito_clave)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    if domicilio_id is not None:
        domicilio = get_domicilio(db, domicilio_id)
        consulta = consulta.filter(Oficina.domicilio == domicilio)
    if es_jurisdiccional is not None:
        consulta = consulta.filter_by(es_jurisdiccional=es_jurisdiccional)
    return consulta.filter_by(estatus="A").order_by(Oficina.id)


def get_oficina(db: Session, oficina_id: int) -> Oficina:
    """Consultar una oficina por su id"""
    oficina = db.query(Oficina).get(oficina_id)
    if oficina is None:
        raise MyNotExistsError("No existe ese oficina")
    if oficina.estatus != "A":
        raise MyIsDeletedError("No es activo ese oficina, está eliminado")
    return oficina


def get_oficina_with_clave(db: Session, clave: str) -> Oficina:
    """Consultar una oficina por su clave"""
    try:
        clave = safe_clave(clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    oficina = db.query(Oficina).filter_by(clave=clave).first()
    if oficina is None:
        raise MyNotExistsError("No existe ese oficina")
    if oficina.estatus != "A":
        raise MyIsDeletedError("No es activo ese oficina, está eliminado")
    return oficina
