"""
Archivo - Remesas Documentos v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.arc_remesas_documentos.models import ArcRemesaDocumento
from ..arc_documentos.crud import get_arc_documento
from ..arc_remesas.crud import get_arc_remesa


def get_arc_remesas_documentos(
    database: Session,
    arc_documento_id: int = None,
    arc_remesa_id: int = None,
) -> Any:
    """Consultar los documentos de las remesas activos"""
    consulta = database.query(ArcRemesaDocumento)
    if arc_documento_id is not None:
        arc_documento = get_arc_documento(database, arc_documento_id)
        consulta = consulta.filter_by(arc_documento_id=arc_documento.id)
    if arc_remesa_id is not None:
        arc_remesa = get_arc_remesa(database, arc_remesa_id)
        consulta = consulta.filter_by(arc_remesa_id=arc_remesa.id)
    return consulta.filter_by(estatus="A").order_by(ArcRemesaDocumento.id.desc())


def get_arc_remesa_documento(database: Session, arc_remesa_documento_id: int) -> ArcRemesaDocumento:
    """Consultar un documento de una remesa por su id"""
    arc_remesa_documento = database.query(ArcRemesaDocumento).get(arc_remesa_documento_id)
    if arc_remesa_documento is None:
        raise MyNotExistsError("No existe ese documento de una remesa")
    if arc_remesa_documento.estatus != "A":
        raise MyIsDeletedError("No es activo ese documento de una remesa, está eliminado")
    return arc_remesa_documento
