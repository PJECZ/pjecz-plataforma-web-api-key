"""
REDAM (Registro Estatal de Deudores Alimentarios Morosos) v3, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemRedamOut(BaseModel):
    """Esquema para entregar deudores alimentarios morosos"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    nombre: str = Field(None)
    expediente: str = Field(None)
    fecha: date = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneRedamOut(ItemRedamOut, OneBaseOut):
    """Esquema para entregar un deudor alimentario moroso"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    autoridad_id: int = Field(None)
    autoridad_descripcion: str = Field(None)
    observaciones: str = Field(None)
