"""
Usuarios v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_email, safe_string

from ...core.usuarios.models import Usuario


def get_usuarios(
    db: Session,
    email: str = None,
    nombres: str = None,
    apellido_paterno: str = None,
    apellido_materno: str = None,
) -> Any:
    """Consultar los usuarios activos"""
    consulta = db.query(Usuario)
    if email is not None:
        try:
            email = safe_email(email, search_fragment=True)
        except ValueError as error:
            raise MyNotValidParamError("El email no es válido") from error
        consulta = consulta.filter(Usuario.email.contains(email))
    if nombres is not None:
        nombres = safe_string(nombres)
        if nombres != "":
            consulta = consulta.filter(Usuario.nombres.contains(nombres))
    if apellido_paterno is not None:
        apellido_paterno = safe_string(apellido_paterno)
        if apellido_paterno != "":
            consulta = consulta.filter(Usuario.apellido_paterno.contains(apellido_paterno))
    if apellido_materno is not None:
        apellido_materno = safe_string(apellido_materno)
        if apellido_materno != "":
            consulta = consulta.filter(Usuario.apellido_materno.contains(apellido_materno))
    return consulta.filter_by(estatus="A").order_by(Usuario.email)


def get_usuario(db: Session, usuario_id: int) -> Usuario:
    """Consultar un usuario por su id"""
    usuario = db.query(Usuario).get(usuario_id)
    if usuario is None:
        raise MyNotExistsError("No existe ese usuario")
    if usuario.estatus != "A":
        raise MyIsDeletedError("No es activo ese usuario, está eliminado")
    return usuario


def get_usuario_by_email(db: Session, email: str) -> Usuario:
    """Consultar un usuario por su email"""
    try:
        email = safe_email(email)
    except ValueError as error:
        raise MyNotValidParamError("El email no es válido") from error
    usuario = db.query(Usuario).filter_by(email=email).first()
    if usuario is None:
        raise MyNotExistsError("No existe ese usuario")
    if usuario.estatus != "A":
        raise MyIsDeletedError("No es activo ese usuario, está eliminado")
    return usuario
