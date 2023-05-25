"""
Centros de Trabajo v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.centros_trabajos.models import CentroTrabajo
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..domicilios.crud import get_domicilio


def get_centros_trabajos(
    db: Session,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
) -> Any:
    """Consultar los centros de trabajos activos"""
    consulta = db.query(CentroTrabajo)
    if distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(db, distrito_clave)
        consulta = consulta.filter_by(distrito_id=distrito.id)
    if domicilio_id is not None:
        domicilio = get_domicilio(db, domicilio_id)
        consulta = consulta.filter_by(domicilio_id=domicilio.id)
    return consulta.filter_by(estatus="A").order_by(CentroTrabajo.id)


def get_centro_trabajo(db: Session, centro_trabajo_id: int) -> CentroTrabajo:
    """Consultar un centro de trabajo por su id"""
    centro_trabajo = db.query(CentroTrabajo).get(centro_trabajo_id)
    if centro_trabajo is None:
        raise MyNotExistsError("No existe ese centro de trabajo")
    if centro_trabajo.estatus != "A":
        raise MyIsDeletedError("No es activo ese centro de trabajo, está eliminado")
    return centro_trabajo


def get_centro_trabajo_with_clave(db: Session, centro_trabajo_clave: str) -> CentroTrabajo:
    """Consultar un centro de trabajo por su clave"""
    try:
        clave = safe_clave(centro_trabajo_clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    centro_trabajo = db.query(CentroTrabajo).filter_by(clave=clave).first()
    if centro_trabajo is None:
        raise MyNotExistsError("No existe ese centro de trabajo")
    if centro_trabajo.estatus != "A":
        raise MyIsDeletedError("No es activo ese centro de trabajo, está eliminado")
    return centro_trabajo
