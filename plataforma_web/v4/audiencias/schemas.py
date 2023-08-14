"""
Audiencias v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class AudienciaIn(BaseModel):
    """Esquema para recibir un audiencia"""

    autoridad_id: int | None
    tiempo: datetime | None
    tipo_audiencia: str | None
    expediente: str | None
    actores: str | None
    demandados: str | None
    sala: str | None
    caracter: str | None
    causa_penal: str | None
    delitos: str | None
    toca: str | None
    expediente_origen: str | None
    imputados: str | None
    origen: str | None


class AudienciaOut(AudienciaIn):
    """Esquema para entregar audiencias"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    creado: datetime | None
    model_config = ConfigDict(from_attributes=True)


class OneAudienciaOut(AudienciaOut, OneBaseOut):
    """Esquema para entregar un audiencia"""
