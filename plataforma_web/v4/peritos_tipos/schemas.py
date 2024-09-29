"""
Tipos de Peritos v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemPeritoTipoOut(BaseModel):
    """Esquema para entregar tipos de peritos"""

    id: int = Field(None)
    nombre: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OnePeritoTipoOut(ItemPeritoTipoOut, OneBaseOut):
    """Esquema para entregar un tipo de perito"""
