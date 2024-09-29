"""
Glosas v4, CRUD (create, read, update, and delete)
"""

from datetime import date
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_expediente
from plataforma_web.core.autoridades.models import Autoridad
from plataforma_web.core.glosas.models import Glosa
from plataforma_web.v4.autoridades.crud import get_autoridad, get_autoridad_with_clave
from plataforma_web.v4.distritos.crud import get_distrito, get_distrito_with_clave


def get_glosas(
    database: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    expediente: str = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
) -> Any:
    """Consultar las glosas"""
    consulta = database.query(Glosa)
    if autoridad_id is not None:
        autoridad = get_autoridad(database, autoridad_id)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif autoridad_clave is not None:
        autoridad = get_autoridad_with_clave(database, autoridad_clave)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif distrito_id is not None:
        distrito = get_distrito(database, distrito_id)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(database, distrito_clave)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    if expediente is not None:
        try:
            expediente = safe_expediente(expediente)
        except (IndexError, ValueError) as error:
            raise MyNotValidParamError("El expediente no es válido") from error
        consulta = consulta.filter_by(expediente=expediente)
    if fecha is not None:
        consulta = consulta.filter(Glosa.fecha == fecha)
    else:
        if fecha_desde is not None:
            consulta = consulta.filter(Glosa.fecha >= fecha_desde)
        if fecha_hasta is not None:
            consulta = consulta.filter(Glosa.fecha <= fecha_hasta)
    return consulta.filter_by(estatus="A").order_by(Glosa.id.desc())


def get_glosa(database: Session, glosa_id: int) -> Glosa:
    """Consultar un glosa por su id"""
    glosa = database.query(Glosa).get(glosa_id)
    if glosa is None:
        raise MyNotExistsError("No existe ese glosa")
    if glosa.estatus != "A":
        raise MyIsDeletedError("No es activo ese glosa, está eliminado")
    return glosa
