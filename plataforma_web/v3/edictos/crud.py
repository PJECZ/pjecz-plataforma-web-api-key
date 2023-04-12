"""
Edictos v3, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError

from ...core.autoridades.models import Autoridad
from ...core.edictos.models import Edicto
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave


def get_edictos(
    db: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
) -> Any:
    """Consultar los edictos activos"""
    consulta = db.query(Edicto)
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
        consulta = consulta.filter(Edicto.fecha == fecha)
    elif anio is not None:
        desde = date(year=anio, month=1, day=1)
        hasta = date(year=anio, month=12, day=31)
        consulta = consulta.filter(Edicto.fecha >= desde).filter(Edicto.fecha <= hasta)
    return consulta.filter_by(estatus="A").order_by(Edicto.id)


def get_edicto(db: Session, edicto_id: int) -> Edicto:
    """Consultar un edicto por su id"""
    edicto = db.query(Edicto).get(edicto_id)
    if edicto is None:
        raise MyNotExistsError("No existe ese edicto")
    if edicto.estatus != "A":
        raise MyIsDeletedError("No es activo ese edicto, está eliminado")
    return edicto


def create_edicto(db: Session, edicto: Edicto) -> Edicto:
    """Crear un edicto"""

    # Validar autoridad
    if edicto.autoridad_id is None:
        raise MyNotValidParamError("No se especificó la autoridad")
    autoridad = get_autoridad(db=db, autoridad_id=edicto.autoridad_id)
    edicto.autoridad_id = autoridad.id

    # Crear
    db.add(edicto)
    db.commit()
    db.refresh(edicto)

    # Entregar
    return edicto


def update_edicto(db: Session, edicto_id: int, edicto_in: Edicto) -> Edicto:
    """Actualizar un edicto"""
    edicto = get_edicto(db=db, edicto_id=edicto_id)

    # Validar autoridad, si se especificó y se cambió
    if edicto_in.autoridad_id is not None and edicto.autoridad_id != edicto_in.autoridad_id:
        autoridad = get_autoridad(db=db, autoridad_id=edicto_in.autoridad_id)
        edicto.autoridad_id = autoridad.autoridad_id

    # Actualizar las columnas
    edicto.fecha = edicto_in.fecha
    edicto.descripcion = edicto_in.descripcion
    edicto.expediente = edicto_in.expediente
    edicto.numero_publicacion = edicto_in.numero_publicacion
    edicto.archivo = edicto_in.archivo
    edicto.url = edicto_in.url

    # Actualizar
    db.add(edicto)
    db.commit()
    db.refresh(edicto)

    # Entregar
    return edicto


def delete_edicto(db: Session, edicto_id: int) -> Edicto:
    """Eliminar un edicto"""
    edicto = get_edicto(db=db, edicto_id=edicto_id)
    edicto.estatus = "B"
    db.add(edicto)
    db.commit()
    db.refresh(edicto)
    return edicto
