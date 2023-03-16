"""
Entradas-Salidas v3, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.entradas_salidas.models import EntradaSalida
from ..usuarios.crud import get_usuario


def get_entradas_salidas(db: Session, usuario_id: int = None) -> Any:
    """Consultar los entradas-salidas activos"""
    consulta = db.query(EntradaSalida)
    if usuario_id is not None:
        usuario = get_usuario(db, usuario_id)
        consulta = consulta.filter(usuario == usuario)
    return consulta.filter_by(estatus="A").order_by(EntradaSalida.id.desc())


def get_entrada_salida(db: Session, entrada_salida_id: int) -> EntradaSalida:
    """Consultar un entrada-salida por su id"""
    entrada_salida = db.query(EntradaSalida).get(entrada_salida_id)
    if entrada_salida is None:
        raise MyNotExistsError("No existe ese entrada-salida")
    if entrada_salida.estatus != "A":
        raise MyIsDeletedError("No es activo ese entrada-salida, está eliminado")
    return entrada_salida
