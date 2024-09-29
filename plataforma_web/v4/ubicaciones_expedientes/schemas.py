"""
Ubicaciones de Expedientes v4, esquemas de pydantic
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemUbicacionExpedienteOut(BaseModel):
    """Esquema para entregar ubicaciones de expedientes"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    expediente: str = Field(None)
    ubicacion: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneUbicacionExpedienteOut(ItemUbicacionExpedienteOut, OneBaseOut):
    """Esquema para entregar una ubicacion de expediente"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    autoridad_descripcion: str = Field(None)
