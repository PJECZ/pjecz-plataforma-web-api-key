"""
Archivo - Documentos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcDocumentoOut(BaseModel):
    """Esquema para entregar documentos"""

    id: int | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    autoridad_clave: str | None = None
    autoridad_descripcion: str | None = None
    autoridad_descripcion_corta: str | None = None
    arc_juzgado_origen_id: int | None = None
    arc_juzgado_origen_clave: str | None = None
    arc_juzgado_origen_descripcion: str | None = None
    arc_juzgado_origen_descripcion_corta: str | None = None
    actor: str | None = None
    anio: int | None = None
    demandado: str | None = None
    expediente: str | None = None
    juicio: str | None = None
    fojas: int | None = None
    tipo_juzgado: str | None = None
    ubicacion: str | None = None
    tipo: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneArcDocumentoOut(ArcDocumentoOut, OneBaseOut):
    """Esquema para entregar un documento"""
