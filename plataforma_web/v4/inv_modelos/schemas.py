"""
Inventarios Modelos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvModeloOut(BaseModel):
    """Esquema para entregar modelos"""

    id: int | None = None
    inv_marca_id: int | None = None
    inv_marca_nombre: str | None = None
    descripcion: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneInvModeloOut(InvModeloOut, OneBaseOut):
    """Esquema para entregar un modelo"""
