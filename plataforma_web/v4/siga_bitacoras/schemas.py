"""
SIGA Bitacoras v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class SIGABitacoraOut(BaseModel):
    """Esquema para entregar bitacoras"""

    id: int | None = None
    siga_sala_id: int | None = None
    siga_sala_clave: str | None = None
    accion: str | None = None
    estado: str | None = None
    descripcion: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneSIGABitacoraOut(SIGABitacoraOut, OneBaseOut):
    """Esquema para entregar una bitacora"""
