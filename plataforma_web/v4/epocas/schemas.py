"""
Epocas v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemEpocaOut(BaseModel):
    """Esquema para entregar epocas"""

    id: int = Field(None)
    nombre: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneEpocaOut(ItemEpocaOut, OneBaseOut):
    """Esquema para entregar una epoca"""
