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
    fecha_desde: date = None,
    fecha_hasta: date = None,
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
    if anio is not None:
        desde = date(year=anio, month=1, day=1)
        hasta = date(year=anio, month=12, day=31)
        consulta = consulta.filter(Sentencia.fecha >= desde).filter(Sentencia.fecha <= hasta)
    elif fecha is not None:
        consulta = consulta.filter(Sentencia.fecha == fecha)
    else:
        if fecha_desde is not None:
            consulta = consulta.filter(Sentencia.fecha >= fecha_desde)
        if fecha_hasta is not None:
            consulta = consulta.filter(Sentencia.fecha <= fecha_hasta)
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


def create_sentencia(db: Session, sentencia: Sentencia) -> Sentencia:
    """Crear una nueva sentencia"""

    # Validar autoridad
    get_autoridad(db, sentencia.autoridad_id)

    # Validar materia_tipo_juicio
    get_materia_tipo_juicio(db, sentencia.materia_tipo_juicio_id)

    # Guardar
    db.add(sentencia)
    db.commit()
    db.refresh(sentencia)

    # Entregar
    return sentencia


def update_sentencia(db: Session, sentencia_id: int, sentencia_in: Sentencia) -> Sentencia:
    """Modificar una sentencia"""

    # Consultar la sentencia
    sentencia = get_sentencia(db, sentencia_id)

    # Validad autoridad, si se especificó y es diferente
    if sentencia_in.autoridad_id is not None and sentencia_in.autoridad_id != sentencia.autoridad_id:
        autoridad = get_autoridad(db, sentencia_in.autoridad_id)
        sentencia.autoridad_id = autoridad.id

    # Validad materia_tipo_juicio, si se especificó y es diferente
    if sentencia_in.materia_tipo_juicio_id is not None and sentencia_in.materia_tipo_juicio_id != sentencia.materia_tipo_juicio_id:
        materia_tipo_juicio = get_materia_tipo_juicio(db, sentencia_in.materia_tipo_juicio_id)
        sentencia.materia_tipo_juicio_id = materia_tipo_juicio.id

    # Actualizar las columnas
    sentencia.sentencia = sentencia_in.sentencia
    sentencia.sentencia_fecha = sentencia_in.sentencia_fecha
    sentencia.expediente = sentencia_in.expediente
    sentencia.fecha = sentencia_in.fecha
    sentencia.descripcion = sentencia_in.descripcion
    sentencia.es_perspectiva_genero = sentencia_in.es_perspectiva_genero
    sentencia.archivo = sentencia_in.archivo
    sentencia.url = sentencia_in.url

    # Guardar
    db.add(sentencia)
    db.commit()
    db.refresh(sentencia)

    # Entregar
    return sentencia


def delete_sentencia(db: Session, sentencia_id: int) -> Sentencia:
    """Borrar una sentencia"""
    sentencia = get_sentencia(db, sentencia_id)
    sentencia.estatus = "B"
    db.add(sentencia)
    db.commit()
    db.refresh(sentencia)
    return sentencia
