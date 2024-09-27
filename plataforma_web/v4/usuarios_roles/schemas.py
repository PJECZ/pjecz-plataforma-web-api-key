"""
Usuarios-Roles v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemUsuarioRolOut(BaseModel):
    """Esquema para entregar usuarios-roles"""

    id: int = Field(None)
    rol_nombre: str = Field(None)
    usuario_email: str = Field(None)
    descripcion: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneUsuarioRolOut(ItemUsuarioRolOut, OneBaseOut):
    """Esquema para entregar un usuario-rol"""

    rol_id: int = Field(None)
    usuario_id: int = Field(None)
