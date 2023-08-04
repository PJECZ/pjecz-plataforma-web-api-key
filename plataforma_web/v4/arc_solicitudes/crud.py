"""
Archivo - Solicitudes v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_string

from ...core.arc_solicitudes.models import ArcSolicitud
from ...core.autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave


def get_arc_solicitudes(
    database: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    estado: str = None,
) -> Any:
    """Consultar las solicitudes activas"""
    consulta = database.query(ArcSolicitud)
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
    if estado is not None:
        estado = safe_string(estado)
        if estado in ArcSolicitud.ESTADOS:
            consulta = consulta.filter_by(estado=estado)
        else:
            raise MyNotValidParamError("No es válido el estado")
    return consulta.filter_by(estatus="A").order_by(ArcSolicitud.id)


def get_arc_solicitud(database: Session, arc_solicitud_id: int) -> ArcSolicitud:
    """Consultar una solicitud por su id"""
    arc_solicitud = database.query(ArcSolicitud).get(arc_solicitud_id)
    if arc_solicitud is None:
        raise MyNotExistsError("No existe ese solicitud")
    if arc_solicitud.estatus != "A":
        raise MyIsDeletedError("No es activo ese solicitud, está eliminado")
    return arc_solicitud
