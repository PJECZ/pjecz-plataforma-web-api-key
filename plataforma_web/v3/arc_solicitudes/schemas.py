"""
Archivo - Solicitudes v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class ArcSolicitudOut(BaseModel):
    """Esquema para entregar solicitudes"""

    id: int | None
    arc_documento_id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    usuario_asignado_id: int | None
    usuario_asignado_email: str | None
    usuario_asignado_nombre: str | None
    usuario_receptor_id: int | None
    esta_archivado: bool | None
    num_folio: str | None
    tiempo_recepcion: datetime | None
    fojas: int | None
    estado: str | None
    razon: str | None
    observaciones_solicitud: str | None
    observaciones_razon: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneArcSolicitudOut(ArcSolicitudOut, OneBaseOut):
    """Esquema para entregar un solicitud"""
