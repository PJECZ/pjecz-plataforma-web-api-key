"""
SIGA Bitacoras v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class SIGABitacoraOut(BaseModel):
    """Esquema para entregar bitacoras"""

    id: int | None
    siga_sala_id: int | None
    siga_sala_clave: str | None
    accion: str | None
    estado: str | None
    descripcion: str | None
    model_config = ConfigDict(from_attributes=True)


class OneSIGABitacoraOut(SIGABitacoraOut, OneBaseOut):
    """Esquema para entregar una bitacora"""
