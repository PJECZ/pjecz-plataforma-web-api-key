"""
Inventarios Categorias v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvCategoriaOut(BaseModel):
    """Esquema para entregar categorias"""

    id: int | None = None
    nombre: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneInvCategoriaOut(InvCategoriaOut, OneBaseOut):
    """Esquema para entregar una categoria"""
