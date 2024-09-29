"""
Audiencias v4, esquemas de pydantic
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemAudienciaOut(BaseModel):
    """Esquema para entregar audiencias"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    autoridad_id: int = Field(None)
    autoridad_clave: str = Field(None)
    autoridad_descripcion_corta: str = Field(None)
    tiempo: datetime = Field(None)
    tipo_audiencia: str = Field(None)
    expediente: str = Field(None)
    actores: str = Field(None)
    demandados: str = Field(None)
    sala: str = Field(None)
    caracter: str = Field(None)
    causa_penal: str = Field(None)
    delitos: str = Field(None)
    toca: str = Field(None)
    expediente_origen: str = Field(None)
    imputados: str = Field(None)
    origen: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneAudienciaOut(ItemAudienciaOut, OneBaseOut):
    """Esquema para entregar una audiencia"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    autoridad_descripcion: str = Field(None)
