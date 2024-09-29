"""
Edictos v4, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemEdictoOut(BaseModel):
    """Esquema para entregar edictos"""

    id: int = Field(None)
    autoridad_id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    fecha: date = Field(None)
    descripcion: str = Field(None)
    expediente: str = Field(None)
    numero_publicacion: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneEdictoOut(ItemEdictoOut, OneBaseOut):
    """Esquema para entregar un edicto"""

    distrito_id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_descripcion: str = Field(None)
    archivo: str = Field(None)
    url: str = Field(None)
