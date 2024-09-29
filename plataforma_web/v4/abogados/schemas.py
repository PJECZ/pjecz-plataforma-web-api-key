"""
Abogados v4, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemAbogadoOut(BaseModel):
    """Esquema para entregar abogados"""

    id: int = Field(None)
    fecha: date = Field(None)
    numero: str = Field(None)
    libro: str = Field(None)
    nombre: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneAbogadoOut(ItemAbogadoOut, OneBaseOut):
    """Esquema para entregar un abogado"""
