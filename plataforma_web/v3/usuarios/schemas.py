"""
Usuarios v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class UsuarioOut(BaseModel):
    """Esquema para entregar usuarios"""

    id: int | None
    email: str | None
    nombres: str | None
    apellido_paterno: str | None
    apellido_materno: str | None
    curp: str | None
    puesto: str | None
    telefono: str | None
    extension: str | None
    workspace: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneUsuarioOut(UsuarioOut, OneBaseOut):
    """Esquema para entregar un usuario"""


class UsuarioInDB(UsuarioOut):
    """Usuario en base de datos"""

    username: str
    permissions: dict
    hashed_password: str
    disabled: bool
    api_key: str
    api_key_expiracion: datetime
