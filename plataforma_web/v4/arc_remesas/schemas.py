"""
Archivo - Remesas v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcRemesaOut(BaseModel):
    """Esquema para entregar remesas"""

    id: int | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    autoridad_clave: str | None = None
    autoridad_descripcion: str | None = None
    autoridad_descripcion_corta: str | None = None
    usuario_asignado_id: int | None = None
    usuario_asignado_email: str | None = None
    usuario_asignado_nombre: str | None = None
    anio: str | None = None
    esta_archivado: bool | None = None
    num_oficio: str | None = None
    rechazo: str | None = None
    tiempo_enviado: datetime | None = None
    num_documentos: int | None = None
    num_anomalias: int | None = None
    razon: str | None = None
    estado: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneArcRemesaOut(ArcRemesaOut, OneBaseOut):
    """Esquema para entregar un remesa"""
