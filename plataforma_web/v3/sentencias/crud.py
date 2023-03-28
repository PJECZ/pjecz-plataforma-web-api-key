"""
Sentencias v3, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError

from ...core.autoridades.models import Autoridad
from ...core.sentencias.models import Sentencia
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..materias_tipos_juicios.crud import get_materia_tipo_juicio


def get_sentencias(
    db: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
    materia_tipo_juicio_id: int = None,
) -> Any:
    """Consultar los sentencias activos"""
    consulta = db.query(Sentencia)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif autoridad_clave is not None:
        autoridad = get_autoridad_with_clave(db, autoridad_clave)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(db, distrito_clave)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito_id == distrito.id)
    if fecha is not None:
        consulta = consulta.filter(Sentencia.fecha == fecha)
    elif anio is not None:
        if 1900 <= anio <= date.today().year:
            consulta = consulta.filter(Sentencia.fecha >= date(anio, 1, 1)).filter(Sentencia.fecha <= date(anio, 12, 31))
        else:
            raise MyNotValidParamError("El año no es válido")
    if materia_tipo_juicio_id is not None:
        materia_tipo_juicio = get_materia_tipo_juicio(db, materia_tipo_juicio_id)
        consulta = consulta.filter_by(materia_tipo_juicio_id=materia_tipo_juicio.id)
    return consulta.filter_by(estatus="A").order_by(Sentencia.id)


def get_sentencia(db: Session, sentencia_id: int) -> Sentencia:
    """Consultar un sentencia por su id"""
    sentencia = db.query(Sentencia).get(sentencia_id)
    if sentencia is None:
        raise MyNotExistsError("No existe ese sentencia")
    if sentencia.estatus != "A":
        raise MyIsDeletedError("No es activo ese sentencia, está eliminado")
    return sentencia
