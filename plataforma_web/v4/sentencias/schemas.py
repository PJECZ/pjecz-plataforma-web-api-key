"""
Sentencias v4, esquemas de pydantic
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemSentenciaOut(BaseModel):
    """Esquema para entregar sentencias"""

    id: int = Field(None)
    autoridad_id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    materia_nombre: str = Field(None)
    materia_tipo_juicio_descripcion: str = Field(None)
    sentencia: str = Field(None)
    sentencia_fecha: date = Field(None)
    expediente: str = Field(None)
    fecha: date = Field(None)
    descripcion: str = Field(None)
    es_perspectiva_genero: bool = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneSentenciaOut(ItemSentenciaOut, OneBaseOut):
    """Esquema para entregar una sentencia"""

    distrito_id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_descripcion: str = Field(None)
    materia_id: int = Field(None)
    materia_tipo_juicio_id: int = Field(None)
    expediente_anio: int = Field(None)
    expediente_num: int = Field(None)
    archivo: str = Field(None)
    url: str = Field(None)
