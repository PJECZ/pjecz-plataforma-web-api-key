"""
Bitacoras v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_email

from ...core.bitacoras.models import Bitacora
from ...core.usuarios.models import Usuario
from ..modulos.crud import get_modulo, get_modulo_with_nombre
from ..usuarios.crud import get_usuario


def get_bitacoras(
    db: Session,
    modulo_id: int = None,
    modulo_nombre: str = None,
    usuario_id: int = None,
    usuario_email: str = None,
) -> Any:
    """Consultar las bitacoras activas"""
    consulta = db.query(Bitacora)
    if modulo_id is not None:
        modulo = get_modulo(db, modulo_id)
        consulta = consulta.filter(modulo == modulo)
    elif modulo_nombre is not None:
        modulo = get_modulo_with_nombre(db, modulo_nombre)
        consulta = consulta.filter(modulo == modulo)
    if usuario_id is not None:
        usuario = get_usuario(db, usuario_id)
        consulta = consulta.filter(usuario == usuario)
    if usuario_email is not None:
        try:
            usuario_email = safe_email(usuario_email, search_fragment=True)
        except ValueError as error:
            raise MyNotValidParamError("El email no es válido") from error
        consulta = consulta.join(Usuario).filter(Usuario.email.ilike(usuario_email))
    return consulta.filter_by(estatus="A").order_by(Bitacora.id.desc())


def get_bitacora(db: Session, bitacora_id: int) -> Bitacora:
    """Consultar una bitacora por su id"""
    bitacora = db.query(Bitacora).get(bitacora_id)
    if bitacora is None:
        raise MyNotExistsError("No existe ese bitacora")
    if bitacora.estatus != "A":
        raise MyIsDeletedError("No es activo ese bitacora, está eliminado")
    return bitacora
