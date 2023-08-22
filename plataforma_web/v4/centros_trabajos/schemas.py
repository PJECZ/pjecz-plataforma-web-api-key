"""
Centros de Trabajo v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class CentroTrabajoListOut(BaseModel):
    """Esquema para entregar centros de trabajo como listado"""

    id: int | None = None
    clave: str | None = None
    model_config = ConfigDict(from_attributes=True)


class CentroTrabajoOut(CentroTrabajoListOut):
    """Esquema para entregar centros de trabajo como paginado"""

    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    domicilio_id: int | None = None
    domicilio_completo: str | None = None
    domicilio_edificio: str | None = None
    nombre: str | None = None
    telefono: str | None = None


class OneCentroTrabajoOut(CentroTrabajoOut, OneBaseOut):
    """Esquema para entregar un centro de trabajo"""
