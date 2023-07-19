"""
Inventarios Marcas v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvMarcaOut(BaseModel):
    """Esquema para entregar marcas"""

    id: int | None
    nombre: str | None
    model_config = ConfigDict(from_attributes=True)


class OneInvMarcaOut(InvMarcaOut, OneBaseOut):
    """Esquema para entregar un marca"""
