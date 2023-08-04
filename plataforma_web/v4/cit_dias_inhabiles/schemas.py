"""
Citas Dias Inhabiles v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class CitDiaInhabilIn(BaseModel):
    """Esquema para recibir un dia inhabil"""

    fecha: date | None
    descripcion: str | None


class CitDiaInhabilOut(CitDiaInhabilIn):
    """Esquema para entregar dias inhabiles"""

    id: int | None
    model_config = ConfigDict(from_attributes=True)


class OneCitDiaInhabilOut(CitDiaInhabilOut, OneBaseOut):
    """Esquema para entregar un dia inhabil"""
