"""
Sentencias v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class SentenciaIn(BaseModel):
    """Esquema para recibir una sentencia"""

    autoridad_id: int | None
    materia_tipo_juicio_id: int | None
    sentencia: str | None
    sentencia_fecha: date | None
    expediente: str | None
    fecha: date | None
    descripcion: str | None
    es_perspectiva_genero: bool | None
    archivo: str | None
    url: str | None
    descargar_url: str | None


class SentenciaOut(SentenciaIn):
    """Esquema para entregar sentencias"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    expediente_anio: int | None
    expediente_num: int | None
    materia_id: int | None
    materia_nombre: str | None
    materia_tipo_juicio_descripcion: str | None
    creado: datetime | None
    model_config = ConfigDict(from_attributes=True)


class OneSentenciaOut(SentenciaOut, OneBaseOut):
    """Esquema para entregar una sentencia"""
