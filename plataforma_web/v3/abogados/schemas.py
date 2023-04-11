"""
Abogados v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class AbogadoIn(BaseModel):
    """Esquema para recibir un abogado"""

    fecha: date | None
    numero: str | None
    libro: str | None
    nombre: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class AbogadoOut(AbogadoIn):
    """Esquema para entregar abogados"""

    id: int | None


class OneAbogadoOut(AbogadoOut, OneBaseOut):
    """Esquema para entregar un abogado"""
