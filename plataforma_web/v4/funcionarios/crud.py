"""
Funcionarios v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.centros_trabajos.models import CentroTrabajo
from ...core.domicilios.models import Domicilio
from ...core.funcionarios.models import Funcionario
from ..centros_trabajos.crud import get_centro_trabajo
from ..distritos.crud import get_distrito, get_distrito_with_clave
from ..domicilios.crud import get_domicilio


def get_funcionarios(
    database: Session,
    centro_trabajo_id: int = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
    en_funciones: bool = None,
    en_sentencias: bool = None,
    en_soportes: bool = None,
    en_tesis_jurisprudencias: bool = None,
) -> Any:
    """Consultar los funcionarios activos"""
    consulta = database.query(Funcionario)
    if centro_trabajo_id is not None:
        centro_trabajo = get_centro_trabajo(database, centro_trabajo_id)
        consulta = consulta.filter_by(centro_trabajo=centro_trabajo)
    if distrito_id is not None:
        distrito = get_distrito(database, distrito_id)
        consulta = consulta.join(CentroTrabajo).filter_by(distrito_id=distrito.id)
    elif distrito_clave is not None:
        distrito = get_distrito_with_clave(database, distrito_clave)
        consulta = consulta.join(CentroTrabajo).filter_by(distrito_id=distrito.id)
    if domicilio_id is not None:
        domicilio = get_domicilio(database, domicilio_id)
        consulta = consulta.join(Domicilio).filter_by(domicilio=domicilio)
    if en_funciones is not None:
        consulta = consulta.filter_by(en_funciones=en_funciones)
    if en_sentencias is not None:
        consulta = consulta.filter_by(en_sentencias=en_sentencias)
    if en_soportes is not None:
        consulta = consulta.filter_by(en_soportes=en_soportes)
    if en_tesis_jurisprudencias is not None:
        consulta = consulta.filter_by(en_tesis_jurisprudencias=en_tesis_jurisprudencias)
    return consulta.filter_by(estatus="A").order_by(Funcionario.id.desc())


def get_funcionario(database: Session, funcionario_id: int) -> Funcionario:
    """Consultar un funcionario por su id"""
    funcionario = database.query(Funcionario).get(funcionario_id)
    if funcionario is None:
        raise MyNotExistsError("No existe ese funcionario")
    if funcionario.estatus != "A":
        raise MyIsDeletedError("No es activo ese funcionario, está eliminado")
    return funcionario
