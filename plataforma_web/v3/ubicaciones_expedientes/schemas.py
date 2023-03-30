"""
Ubicaciones de Expedientes v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class UbicacionExpedienteOut(BaseModel):
    """Esquema para entregar ubicaciones de expedientes"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_id: int | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    expediente: str | None
    ubicacion: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneUbicacionExpedienteOut(UbicacionExpedienteOut, OneBaseOut):
    """Esquema para entregar una ubicacion de expediente"""
