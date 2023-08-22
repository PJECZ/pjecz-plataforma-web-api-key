"""
SIGA Salas v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class SIGASalaOut(BaseModel):
    """Esquema para entregar salas"""

    id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    domicilio_id: int | None = None
    domicilio_edificio: str | None = None
    clave: str | None = None
    direccion_ip: str | None = None
    direccion_nvr: str | None = None
    estado: str | None = None
    descripcion: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneSIGASalaOut(SIGASalaOut, OneBaseOut):
    """Esquema para entregar una sala"""
