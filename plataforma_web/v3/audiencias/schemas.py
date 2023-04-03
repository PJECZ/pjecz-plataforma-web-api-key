"""
Audiencias v3, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class AudienciaOut(BaseModel):
    """Esquema para entregar audiencias"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_id: int | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
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

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneAudienciaOut(AudienciaOut, OneBaseOut):
    """Esquema para entregar un audiencia"""
