"""
Tesis Jurisprudencias v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class TesisJurisprudenciaOut(BaseModel):
    """Esquema para entregar tesis jurisprudencias"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_id: int | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    epoca_id: int | None
    epoca_nombre: str | None
    materia_id: int | None
    materia_clave: str | None
    materia_nombre: str | None
    titulo: str | None
    subtitulo: str | None
    tipo: str | None
    estado: str | None
    clave_control: str | None
    clase: str | None
    rubro: str | None
    texto: str | None
    precedentes: str | None
    votacion: str | None
    votos_particulares: str | None
    aprobacion_fecha: date | None
    publicacion_tiempo: datetime | None
    aplicacion_tiempo: datetime | None
    model_config = ConfigDict(from_attributes=True)


class OneTesisJurisprudenciaOut(TesisJurisprudenciaOut, OneBaseOut):
    """Esquema para entregar una tesis jurisprudencia"""
