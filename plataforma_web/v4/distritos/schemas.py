"""
Distritos v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemDistritoOut(BaseModel):
    """Esquema para entregar distritos en listado"""

    id: int = Field(None)
    clave: str = Field(None)
    nombre: str = Field(None)
    nombre_corto: str = Field(None)
    es_distrito_judicial: bool = Field(None)
    es_distrito: bool = Field(None)
    es_jurisdiccional: bool = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneDistritoOut(ItemDistritoOut, OneBaseOut):
    """Esquema para entregar un distrito"""
