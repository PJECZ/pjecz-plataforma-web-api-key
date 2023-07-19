"""
Abogados v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class AbogadoIn(BaseModel):
    """Esquema para recibir un abogado"""

    fecha: date | None
    numero: str | None
    libro: str | None
    nombre: str | None


class AbogadoOut(AbogadoIn):
    """Esquema para entregar abogados"""

    id: int | None
    model_config = ConfigDict(from_attributes=True)


class OneAbogadoOut(AbogadoOut, OneBaseOut):
    """Esquema para entregar un abogado"""
