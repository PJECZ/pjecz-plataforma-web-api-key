"""
Centros de Trabajo v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class CentroTrabajoListOut(BaseModel):
    """Esquema para entregar centros de trabajo como listado"""

    id: int | None
    clave: str | None
    model_config = ConfigDict(from_attributes=True)


class CentroTrabajoOut(CentroTrabajoListOut):
    """Esquema para entregar centros de trabajo como paginado"""

    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    domicilio_id: int | None
    domicilio_completo: str | None
    domicilio_edificio: str | None
    nombre: str | None
    telefono: str | None


class OneCentroTrabajoOut(CentroTrabajoOut, OneBaseOut):
    """Esquema para entregar un centro de trabajo"""
