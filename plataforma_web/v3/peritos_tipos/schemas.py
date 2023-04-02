"""
Peritos - Tipos v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class PeritoTipoOut(BaseModel):
    """Esquema para entregar tipos de peritos"""

    id: int | None
    nombre: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OnePeritoTipoOut(PeritoTipoOut, OneBaseOut):
    """Esquema para entregar un tipo de perito"""
