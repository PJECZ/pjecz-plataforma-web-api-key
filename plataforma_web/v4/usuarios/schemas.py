"""
Usuarios v4, esquemas de pydantic
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemUsuarioOut(BaseModel):
    """Esquema para entregar usuarios"""

    id: int = Field(None)
    email: str = Field(None)
    nombres: str = Field(None)
    apellido_paterno: str = Field(None)
    apellido_materno: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class AuthenticatedUser(ItemUsuarioOut):
    """Usuario en base de datos"""

    username: str
    permissions: dict
    hashed_password: str
    disabled: bool
    api_key: str
    api_key_expiracion: datetime


class OneUsuarioOut(ItemUsuarioOut, OneBaseOut):
    """Esquema para entregar un usuario"""

    distrito_id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    autoridad_directorio_edictos: str = Field(None)
    oficina_id: int = Field(None)
    oficina_clave: str = Field(None)
    email_personal: str = Field(None)
    curp: str = Field(None)
    puesto: str = Field(None)
    telefono: str = Field(None)
    telefono_celular: str = Field(None)
    extension: str = Field(None)
    workspace: str = Field(None)
