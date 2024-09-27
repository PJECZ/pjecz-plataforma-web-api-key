"""
Modulos v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemModuloOut(BaseModel):
    """Esquema para entregar modulos"""

    id: int = Field(None)
    nombre: str = Field(None)
    nombre_corto: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneModuloOut(ItemModuloOut, OneBaseOut):
    """Esquema para entregar un modulo"""

    icono: str = Field(None)
    ruta: str = Field(None)
    en_navegacion: bool = Field(None)
