"""
Peritos v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemPeritoOut(BaseModel):
    """Esquema para entregar peritos"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    perito_tipo_nombre: str = Field(None)
    nombre: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OnePeritoOut(ItemPeritoOut, OneBaseOut):
    """Esquema para entregar un perito"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    perito_tipo_id: int = Field(None)
    domicilio: str = Field(None)
    telefono_fijo: str = Field(None)
    telefono_celular: str = Field(None)
    email: str = Field(None)
    notas: str = Field(None)
