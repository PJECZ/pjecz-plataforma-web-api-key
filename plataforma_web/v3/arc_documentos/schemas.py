"""
Archivo - Documentos v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class ArcDocumentoOut(BaseModel):
    """Esquema para entregar documentos"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    arc_juzgado_origen_id: int | None
    arc_juzgado_origen_clave: str | None
    arc_juzgado_origen_descripcion: str | None
    arc_juzgado_origen_descripcion_corta: str | None
    actor: str | None
    anio: int | None
    demandado: str | None
    expediente: str | None
    juicio: str | None
    fojas: int | None
    tipo_juzgado: str | None
    ubicacion: str | None
    tipo: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneArcDocumentoOut(ArcDocumentoOut, OneBaseOut):
    """Esquema para entregar un documento"""
