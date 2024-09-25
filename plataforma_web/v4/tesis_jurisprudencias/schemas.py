"""
Tesis Jurisprudencias v3, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class TesisJurisprudenciaOut(BaseModel):
    """Esquema para entregar tesis jurisprudencias"""

    id: int | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    autoridad_id: int | None = None
    autoridad_clave: str | None = None
    autoridad_descripcion: str | None = None
    autoridad_descripcion_corta: str | None = None
    epoca_id: int | None = None
    epoca_nombre: str | None = None
    materia_id: int | None = None
    materia_clave: str | None = None
    materia_nombre: str | None = None
    titulo: str | None = None
    subtitulo: str | None = None
    tipo: str | None = None
    estado: str | None = None
    clave_control: str | None = None
    clase: str | None = None
    rubro: str | None = None
    texto: str | None = None
    precedentes: str | None = None
    votacion: str | None = None
    votos_particulares: str | None = None
    aprobacion_fecha: date | None = None
    publicacion_tiempo: datetime | None = None
    aplicacion_tiempo: datetime | None = None
    model_config = ConfigDict(from_attributes=True)


class OneTesisJurisprudenciaOut(TesisJurisprudenciaOut, OneBaseOut):
    """Esquema para entregar una tesis jurisprudencia"""
