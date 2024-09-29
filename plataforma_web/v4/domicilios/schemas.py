"""
Domicilios v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemDomicilioOut(BaseModel):
    """Esquema para entregar domicilios"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    edificio: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneDomicilioOut(ItemDomicilioOut, OneBaseOut):
    """Esquema para entregar un domicilio"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    estado: str = Field(None)
    municipio: str = Field(None)
    calle: str = Field(None)
    num_ext: str = Field(None)
    num_int: str = Field(None)
    colonia: str = Field(None)
    cp: int = Field(None)
    completo: str = Field(None)
