"""
Inventarios Componentes v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvComponenteOut(BaseModel):
    """Esquema para entregar componentes"""

    id: int | None = None
    inv_categoria_id: int | None = None
    inv_categoria_nombre: str | None = None
    inv_equipo_id: int | None = None
    inv_equipo_descripcion: str | None = None
    descripcion: str | None = None
    cantidad: int | None = None
    generacion: str | None = None
    version: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneInvComponenteOut(InvComponenteOut, OneBaseOut):
    """Esquema para entregar un componente"""
