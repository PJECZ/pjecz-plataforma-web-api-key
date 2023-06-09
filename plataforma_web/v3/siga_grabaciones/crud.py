"""
SIGA Grabaciones v3, CRUD (create, read, update, and delete)
"""
import re
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError

from ...core.autoridades.models import Autoridad
from ...core.siga_grabaciones.models import SIGAGrabacion
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..materias.crud import get_materia, get_materia_with_clave
from ..siga_salas.crud import get_siga_sala, get_siga_sala_with_clave

ARCHIVO_NOMBRE_REGEXP = r"(\d\d\d\d-\d\d-\d\d)_(\d\d-\d\d-\d\d)_([A-Z0-1-]{1,16})_([A-Z0-1-]{1,16})_([A-Z]{3})_(\d{1,4}-\d{4}(-[A-Z-]+)?)"


def get_siga_grabaciones(
    db: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    materia_id: int = None,
    materia_clave: str = None,
    siga_sala_id: int = None,
    siga_sala_clave: str = None,
) -> Any:
    """Consultar las grabaciones activas"""
    consulta = db.query(SIGAGrabacion)
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
    if siga_sala_id is not None:
        siga_sala = get_siga_sala(db, siga_sala_id)
        consulta = consulta.filter_by(siga_sala_id=siga_sala.id)
    elif siga_sala_clave is not None:
        siga_sala = get_siga_sala_with_clave(db, siga_sala_clave)
        consulta = consulta.filter_by(siga_sala_id=siga_sala.id)
    if materia_id is not None:
        materia = get_materia(db, materia_id)
        consulta = consulta.filter_by(materia_id=materia.id)
    elif materia_clave is not None:
        materia = get_materia_with_clave(db, materia_clave)
        consulta = consulta.filter_by(materia_id=materia.id)
    return consulta.filter_by(estatus="A").order_by(SIGAGrabacion.id.desc())


def get_siga_grabacion(db: Session, siga_grabacion_id: int) -> SIGAGrabacion:
    """Consultar una grabacion por su id"""
    siga_grabacion = db.query(SIGAGrabacion).get(siga_grabacion_id)
    if siga_grabacion is None:
        raise MyNotExistsError("No existe ese grabacion")
    if siga_grabacion.estatus != "A":
        raise MyIsDeletedError("No es activo ese grabacion, está eliminado")
    return siga_grabacion


def get_siga_grabacion_with_archivo_nombre(db: Session, archivo_nombre: str) -> SIGAGrabacion:
    """Consultar una grabacion por su archivo_nombre"""
    if not re.match(ARCHIVO_NOMBRE_REGEXP, archivo_nombre):
        raise MyNotValidParamError("No es válido ese archivo_nombre")
    siga_grabacion = db.query(SIGAGrabacion).filter_by(archivo_nombre=archivo_nombre).first()
    if siga_grabacion is None:
        raise MyNotExistsError("No existe ese grabacion")
    if siga_grabacion.estatus != "A":
        raise MyIsDeletedError("No es activo ese grabacion, está eliminado")
    return siga_grabacion


def create_siga_grabacion(db: Session, siga_grabacion: SIGAGrabacion) -> SIGAGrabacion:
    """Crear una grabacion"""

    # Validar autoridad, si viene la clave definir el id de la autoridad
    if siga_grabacion.autoridad_id is not None:
        get_autoridad(db, siga_grabacion.autoridad_id)
    elif siga_grabacion.autoridad_clave is not None:
        autoridad = get_autoridad_with_clave(db, siga_grabacion.autoridad_clave)
        siga_grabacion.autoridad_id = autoridad.id

    # Validar materia, si viene la clave definir el id de la materia
    if siga_grabacion.materia_id is not None:
        get_materia(db, siga_grabacion.materia_id)
    elif siga_grabacion.materia_clave is not None:
        materia = get_materia_with_clave(db, siga_grabacion.materia_clave)
        siga_grabacion.materia_id = materia.id

    # Validar sala, si viene la clave definir el id de la sala
    if siga_grabacion.siga_sala_id is not None:
        get_siga_sala(db, siga_grabacion.siga_sala_id)
    elif siga_grabacion.siga_sala_clave is not None:
        siga_sala = get_siga_sala_with_clave(db, siga_grabacion.siga_sala_clave)
        siga_grabacion.siga_sala_id = siga_sala.id

    # Validar expediente

    # Validar inicio

    # Validar termino

    # Validar archivo_nombre

    # Validar justicia_ruta

    # Validar tamanio

    # Validar duracion

    # Validar estado, si no esta definido por defecto es VALIDO
    if siga_grabacion.estado is None:
        siga_grabacion.estado = "VALIDO"
    elif siga_grabacion.estado not in SIGAGrabacion.ESTADOS:
        raise MyNotValidParamError("No esta ese estado en los estados permitidos")

    # Guardar
    db.add(siga_grabacion)
    db.commit()
    db.refresh(siga_grabacion)

    # Entregar
    return siga_grabacion
