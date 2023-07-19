"""
Edictos v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class EdictoIn(BaseModel):
    """Esquema para recibir un edicto"""

    autoridad_id: int | None
    fecha: date | None
    descripcion: str | None
    expediente: str | None
    numero_publicacion: str | None
    archivo: str | None
    url: str | None


class EdictoOut(EdictoIn):
    """Esquema para entregar edictos"""

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


class OneEdictoOut(EdictoOut, OneBaseOut):
    """Esquema para entregar un edicto"""
