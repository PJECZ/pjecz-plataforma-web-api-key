"""
Glosas v3, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_expediente

from ...core.glosas.models import Glosa
from ..autoridades.crud import get_autoridad, get_autoridad_with_clave


def get_glosas(
    db: Session,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    expediente: str = None,
    anio: int = None,
    fecha: date = None,
) -> Any:
    """Consultar los glosas activas"""
    consulta = db.query(Glosa)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    elif autoridad_clave is not None:
        autoridad = get_autoridad_with_clave(db, autoridad_clave)
        consulta = consulta.filter_by(autoridad_id=autoridad.id)
    if expediente is not None:
        try:
            expediente = safe_expediente(expediente)
        except (IndexError, ValueError) as error:
            raise MyNotValidParamError("El expediente no es válido") from error
        consulta = consulta.filter_by(expediente=expediente)
    if fecha is not None:
        consulta = consulta.filter(Glosa.fecha == fecha)
    elif anio is not None:
        if 1900 <= anio <= date.today().year:
            consulta = consulta.filter(Glosa.fecha >= date(anio, 1, 1)).filter(Glosa.fecha <= date(anio, 12, 31))
        else:
            raise MyNotValidParamError("El año no es válido")
    return consulta.filter_by(estatus="A").order_by(Glosa.id)


def get_glosa(db: Session, glosa_id: int) -> Glosa:
    """Consultar un glosa por su id"""
    glosa = db.query(Glosa).get(glosa_id)
    if glosa is None:
        raise MyNotExistsError("No existe ese glosa")
    if glosa.estatus != "A":
        raise MyIsDeletedError("No es activo ese glosa, está eliminado")
    return glosa
