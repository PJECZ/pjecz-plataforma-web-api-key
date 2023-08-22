"""
Archivo - Solicitudes v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcSolicitudOut(BaseModel):
    """Esquema para entregar solicitudes"""

    id: int | None = None
    arc_documento_id: int | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    autoridad_clave: str | None = None
    autoridad_descripcion: str | None = None
    usuario_asignado_id: int | None = None
    usuario_asignado_email: str | None = None
    usuario_asignado_nombre: str | None = None
    usuario_receptor_id: int | None = None
    esta_archivado: bool | None = None
    num_folio: str | None = None
    tiempo_recepcion: datetime | None = None
    fojas: int | None = None
    estado: str | None = None
    razon: str | None = None
    observaciones_solicitud: str | None = None
    observaciones_razon: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneArcSolicitudOut(ArcSolicitudOut, OneBaseOut):
    """Esquema para entregar un solicitud"""
