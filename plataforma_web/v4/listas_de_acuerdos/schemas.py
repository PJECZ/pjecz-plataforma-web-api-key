"""
Listas de Acuerdos v3, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemListaDeAcuerdoOut(BaseModel):
    """Esquema para entregar listas de acuerdos"""

    id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    fecha: date = Field(None)
    descripcion: str = Field(None)
    creado: datetime = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneListaDeAcuerdoOut(ItemListaDeAcuerdoOut, OneBaseOut):
    """Esquema para entregar una lista de acuerdos"""

    distrito_id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_id: int = Field(None)
    autoridad_descripcion: str = Field(None)
    archivo: str = Field(None)
    url: str = Field(None)
