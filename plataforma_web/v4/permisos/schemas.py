"""
Permisos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class PermisoOut(BaseModel):
    """Esquema para entregar permisos"""

    id: int | None
    rol_id: int | None
    rol_nombre: str | None
    modulo_id: int | None
    modulo_nombre: str | None
    nombre: str | None
    nivel: int | None
    model_config = ConfigDict(from_attributes=True)


class OnePermisoOut(PermisoOut, OneBaseOut):
    """Esquema para entregar un permiso"""
