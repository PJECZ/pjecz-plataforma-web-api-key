"""
Archivo - Remesas Documentos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcRemesaDocumentoOut(BaseModel):
    """Esquema para entregar documentos de remesas"""

    id: int | None = None
    arc_documento_id: int | None = None
    arc_remesa_id: int | None = None
    anomalia: str | None = None
    fojas: int | None = None
    observaciones_solicitante: str | None = None
    observaciones_archivista: str | None = None
    tipo_juzgado: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneArcRemesaDocumentoOut(ArcRemesaDocumentoOut, OneBaseOut):
    """Esquema para entregar un documento de una remesa"""
