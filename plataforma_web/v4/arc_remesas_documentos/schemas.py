"""
Archivo - Remesas Documentos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcRemesaDocumentoOut(BaseModel):
    """Esquema para entregar documentos de remesas"""

    id: int | None
    arc_documento_id: int | None
    arc_remesa_id: int | None
    anomalia: str | None
    fojas: int | None
    observaciones_solicitante: str | None
    observaciones_archivista: str | None
    tipo_juzgado: str | None
    model_config = ConfigDict(from_attributes=True)


class OneArcRemesaDocumentoOut(ArcRemesaDocumentoOut, OneBaseOut):
    """Esquema para entregar un documento de una remesa"""
