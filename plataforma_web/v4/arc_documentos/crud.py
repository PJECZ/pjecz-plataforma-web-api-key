"""
Archivo - Documentos v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_string

from ...core.arc_documentos.models import ArcDocumento
from ...core.autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave
from ..distritos.crud import get_distrito, get_distrito_with_clave


def get_arc_documentos(
    database: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    ubicacion: str = None,
) -> Any:
    """Consultar los documentos activos"""
    consulta = database.query(ArcDocumento)
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
    if ubicacion is not None:
        ubicacion = safe_string(ubicacion)
        if ubicacion in ArcDocumento.UBICACIONES:
            consulta = consulta.filter_by(ubicacion=ubicacion)
        else:
            raise MyNotValidParamError("No es válida la ubicación")
    return consulta.filter(ArcDocumento.estatus == "A").order_by(ArcDocumento.id.desc())


def get_arc_documento(database: Session, arc_documento_id: int) -> ArcDocumento:
    """Consultar un documento por su id"""
    arc_documento = database.query(ArcDocumento).get(arc_documento_id)
    if arc_documento is None:
        raise MyNotExistsError("No existe ese documento")
    if arc_documento.estatus != "A":
        raise MyIsDeletedError("No es activo ese documento, está eliminado")
    return arc_documento
