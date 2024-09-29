"""
Roles v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemRolOut(BaseModel):
    """Esquema para entregar roles"""

    id: int = Field(None)
    nombre: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneRolOut(ItemRolOut, OneBaseOut):
    """Esquema para entregar un rol"""
