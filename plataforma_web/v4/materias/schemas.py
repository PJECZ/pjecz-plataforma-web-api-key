"""
Materias v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemMateriaOut(BaseModel):
    """Esquema para entregar materias"""

    id: int = Field(None)
    clave: str = Field(None)
    nombre: str = Field(None)
    en_sentencias: bool = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneMateriaOut(ItemMateriaOut, OneBaseOut):
    """Esquema para entregar una materia"""
