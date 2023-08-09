"""
Epocas v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class EpocaListOut(BaseModel):
    """Esquema para entregar epocas"""

    id: int | None
    nombre: str | None
    model_config = ConfigDict(from_attributes=True)


class EpocaOut(EpocaListOut):
    """Esquema para entregar epocas"""


class OneEpocaOut(EpocaOut, OneBaseOut):
    """Esquema para entregar una epoca"""
