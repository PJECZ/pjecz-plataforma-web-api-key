"""
Usuarios-Roles v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class UsuarioRolOut(BaseModel):
    """Esquema para entregar usuarios-roles"""

    id: int | None
    rol_id: int | None
    rol_nombre: str | None
    usuario_id: int | None
    usuario_nombre: str | None
    descripcion: str | None
    model_config = ConfigDict(from_attributes=True)


class OneUsuarioRolOut(UsuarioRolOut, OneBaseOut):
    """Esquema para entregar un usuario-rol"""
