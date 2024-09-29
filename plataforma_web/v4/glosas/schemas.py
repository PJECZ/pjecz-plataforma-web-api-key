"""
Glosas v4, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemGlosaOut(BaseModel):
    """Esquema para entregar glosas"""

    id: int = Field(None)
    autoridad_id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    fecha: date = Field(None)
    tipo_juicio: str = Field(None)
    descripcion: str = Field(None)
    expediente: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneGlosaOut(ItemGlosaOut, OneBaseOut):
    """Esquema para entregar una glosa"""

    distrito_id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_descripcion: str = Field(None)
    archivo: str = Field(None)
    url: str = Field(None)
