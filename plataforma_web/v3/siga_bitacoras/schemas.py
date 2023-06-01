"""
SIGA Bitacoras v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class SIGABitacoraOut(BaseModel):
    """Esquema para entregar bitacoras"""

    id: int | None
    siga_sala_id: int | None
    siga_sala_clave: str | None
    accion: str | None
    estado: str | None
    descripcion: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneSIGABitacoraOut(SIGABitacoraOut, OneBaseOut):
    """Esquema para entregar una bitacora"""
