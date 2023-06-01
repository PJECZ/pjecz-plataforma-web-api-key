"""
SIGA Bitacoras v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_string

from ...core.siga_bitacoras.models import SIGABitacora
from ..siga_salas.crud import get_siga_sala, get_siga_sala_with_clave


def get_siga_bitacoras(
    db: Session,
    accion: str = None,
    estado: str = None,
    siga_sala_id: int = None,
    siga_sala_clave: str = None,
) -> Any:
    """Consultar los bitacoras activos"""
    consulta = db.query(SIGABitacora)
    if accion is not None:
        accion = safe_string(accion)
        if accion in SIGABitacora.ACCIONES:
            consulta = consulta.filter_by(accion=accion)
        else:
            raise MyNotValidParamError("No es una accion válida")
    if estado is not None:
        estado = safe_string(estado)
        if estado in SIGABitacora.ESTADOS:
            consulta = consulta.filter_by(estado=estado)
        else:
            raise MyNotValidParamError("No es un estado válido")
    if siga_sala_id is not None:
        siga_sala = get_siga_sala(db, siga_sala_id)
        consulta = consulta.filter_by(siga_sala_id=siga_sala.id)
    elif siga_sala_clave is not None:
        siga_sala = get_siga_sala_with_clave(db, siga_sala_clave)
        consulta = consulta.filter_by(siga_sala_id=siga_sala.id)
    return consulta.filter_by(estatus="A").order_by(SIGABitacora.id.desc())


def get_siga_bitacora(db: Session, siga_bitacora_id: int) -> SIGABitacora:
    """Consultar un bitacora por su id"""
    siga_bitacora = db.query(SIGABitacora).get(siga_bitacora_id)
    if siga_bitacora is None:
        raise MyNotExistsError("No existe ese bitacora")
    if siga_bitacora.estatus != "A":
        raise MyIsDeletedError("No es activo ese bitacora, está eliminado")
    return siga_bitacora
