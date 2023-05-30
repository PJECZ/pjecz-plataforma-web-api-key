"""
Archivo - Remesas v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class ArcRemesaOut(BaseModel):
    """Esquema para entregar remesas"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    usuario_asignado_id: int | None
    usuario_asignado_email: str | None
    usuario_asignado_nombre: str | None
    anio: int | None
    esta_archivado: bool | None
    num_oficio: str | None
    rechazo: str | None
    observaciones: str | None
    tiempo_enviado: datetime | None
    tipo_documentos: str | None
    num_documentos: int | None
    num_anomalias: int | None
    razon: str | None
    estado: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneArcRemesaOut(ArcRemesaOut, OneBaseOut):
    """Esquema para entregar un remesa"""
