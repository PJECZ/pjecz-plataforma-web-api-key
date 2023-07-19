"""
SIGA Salas v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave, safe_string

from ...core.oficinas.models import Oficina
from ...core.siga_salas.models import SIGASala
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..domicilios.crud import get_domicilio


def get_siga_salas(
    db: Session,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
    estado: str = None,
) -> Any:
    """Consultar las salas activas"""
    consulta = db.query(SIGASala)
    if distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(db, distrito_clave)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    if domicilio_id is not None:
        domicilio = get_domicilio(db, domicilio_id)
        consulta = consulta.filter(Oficina.domicilio == domicilio)
    if estado is not None:
        estado = safe_string(estado)
        if estado in SIGASala.ESTADOS:
            consulta = consulta.filter_by(estado=estado)
        else:
            raise MyNotValidParamError("No es un estado válido")
    return consulta.filter_by(estatus="A").order_by(SIGASala.clave)


def get_siga_sala(db: Session, siga_sala_id: int) -> SIGASala:
    """Consultar una sala por su id"""
    siga_sala = db.query(SIGASala).get(siga_sala_id)
    if siga_sala is None:
        raise MyNotExistsError("No existe ese sala")
    if siga_sala.estatus != "A":
        raise MyIsDeletedError("No es activo ese sala, está eliminado")
    return siga_sala


def get_siga_sala_with_clave(db: Session, siga_sala_clave: str) -> SIGASala:
    """Consultar una sala por su clave"""
    try:
        clave = safe_clave(siga_sala_clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    siga_sala = db.query(SIGASala).filter_by(clave=clave).first()
    if siga_sala is None:
        raise MyNotExistsError("No existe ese sala")
    if siga_sala.estatus != "A":
        raise MyIsDeletedError("No es activo ese sala, está eliminado")
    return siga_sala
