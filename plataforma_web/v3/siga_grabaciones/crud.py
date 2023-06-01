"""
SIGA Grabaciones v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.autoridades.models import Autoridad
from ...core.siga_grabaciones.models import SIGAGrabacion
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..materias.crud import get_materia
from ..siga_salas.crud import get_siga_sala, get_siga_sala_with_clave


def get_siga_grabaciones(
    db: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
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
    return consulta.filter_by(estatus="A").order_by(SIGAGrabacion.id.desc())


def get_siga_grabacion(db: Session, siga_grabacion_id: int) -> SIGAGrabacion:
    """Consultar una grabacion por su id"""
    siga_grabacion = db.query(SIGAGrabacion).get(siga_grabacion_id)
    if siga_grabacion is None:
        raise MyNotExistsError("No existe ese grabacion")
    if siga_grabacion.estatus != "A":
        raise MyIsDeletedError("No es activo ese grabacion, está eliminado")
    return siga_grabacion


def create_siga_gabacion(db: Session, siga_grabacion: SIGAGrabacion) -> SIGAGrabacion:
    """Crear una grabacion"""

    # Validar autoridad
    if siga_grabacion.autoridad_id is not None:
        get_autoridad(db, siga_grabacion.autoridad_id)
    elif siga_grabacion.autoridad_clave is not None:
        autoridad = get_autoridad_with_clave(db, siga_grabacion.autoridad_clave)
        siga_grabacion.autoridad_id = autoridad.id

    # Validar materia
    get_materia(db, siga_grabacion.materia_id)

    # Validar sala
    if siga_grabacion.siga_sala_id is not None:
        get_siga_sala(db, siga_grabacion.siga_sala_id)
    elif siga_grabacion.siga_sala_clave is not None:
        siga_sala = get_siga_sala_with_clave(db, siga_grabacion.siga_sala_clave)
        siga_grabacion.siga_sala_id = siga_sala.id

    # Guardar
    db.add(siga_grabacion)
    db.commit()
    db.refresh(siga_grabacion)

    # Entregar
    return siga_grabacion
