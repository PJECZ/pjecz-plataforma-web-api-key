"""
Tesis Jurisprudencias v3, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemTesisJurisprudenciaOut(BaseModel):
    """Esquema para entregar tesis jurisprudencias"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    epoca_nombre: str = Field(None)
    materia_clave: str = Field(None)
    materia_nombre: str = Field(None)
    titulo: str = Field(None)
    subtitulo: str = Field(None)
    tipo: str = Field(None)
    estado: str = Field(None)
    clave_control: str = Field(None)
    clase: str = Field(None)
    rubro: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneTesisJurisprudenciaOut(ItemTesisJurisprudenciaOut, OneBaseOut):
    """Esquema para entregar una tesis jurisprudencia"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    autoridad_id: int = Field(None)
    autoridad_descripcion: str = Field(None)
    epoca_id: int = Field(None)
    materia_id: int = Field(None)
    texto: str = Field(None)
    precedentes: str = Field(None)
    votacion: str = Field(None)
    votos_particulares: str = Field(None)
    aprobacion_fecha: date = Field(None)
    publicacion_tiempo: datetime = Field(None)
    aplicacion_tiempo: datetime = Field(None)
