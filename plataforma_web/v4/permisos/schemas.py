"""
Permisos v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemPermisoOut(BaseModel):
    """Esquema para entregar permisos"""

    id: int = Field(None)
    modulo_nombre: str = Field(None)
    rol_nombre: str = Field(None)
    nombre: str = Field(None)
    nivel: int = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OnePermisoOut(ItemPermisoOut, OneBaseOut):
    """Esquema para entregar un permiso"""

    modulo_id: int = Field(None)
    rol_id: int = Field(None)
