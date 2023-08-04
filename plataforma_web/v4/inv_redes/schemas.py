"""
Inventarios Redes v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvRedOut(BaseModel):
    """Esquema para entregar redes"""

    id: int | None
    nombre: str | None
    tipo: str | None
    model_config = ConfigDict(from_attributes=True)


class OneInvRedOut(InvRedOut, OneBaseOut):
    """Esquema para entregar un red"""
