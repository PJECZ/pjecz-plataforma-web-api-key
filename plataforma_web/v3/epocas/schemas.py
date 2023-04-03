"""
Epocas v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class EpocaOut(BaseModel):
    """Esquema para entregar epocas"""

    id: int | None
    nombre: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneEpocaOut(EpocaOut, OneBaseOut):
    """Esquema para entregar una epoca"""
