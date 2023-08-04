"""
Centros de Trabajo v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class CentroTrabajoOut(BaseModel):
    """Esquema para entregar centros de trabajo"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    domicilio_id: int | None
    domicilio_completo: str | None
    domicilio_edificio: str | None
    clave: str | None
    nombre: str | None
    telefono: str | None
    model_config = ConfigDict(from_attributes=True)


class OneCentroTrabajoOut(CentroTrabajoOut, OneBaseOut):
    """Esquema para entregar un centro de trabajo"""
