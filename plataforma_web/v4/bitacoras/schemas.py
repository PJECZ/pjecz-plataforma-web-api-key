"""
Bitacoras v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class BitacoraOut(BaseModel):
    """Esquema para entregar bitacoras"""

    id: int | None = None
    modulo_id: int | None = None
    modulo_nombre: str | None = None
    usuario_id: int | None = None
    usuario_email: str | None = None
    usuario_nombre: str | None = None
    descripcion: str | None = None
    url: str | None = None
    creado: datetime | None = None
    model_config = ConfigDict(from_attributes=True)


class OneBitacoraOut(BitacoraOut, OneBaseOut):
    """Esquema para entregar una bitacora"""
