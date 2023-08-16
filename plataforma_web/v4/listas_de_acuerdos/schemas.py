"""
Listas de Acuerdos v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ListaDeAcuerdoIn(BaseModel):
    """Esquema para recibir una lista de acuerdo"""

    autoridad_id: int | None
    fecha: date | None
    descripcion: str | None
    archivo: str | None
    url: str | None
    descargar_url: str | None


class ListaDeAcuerdoOut(ListaDeAcuerdoIn):
    """Esquema para entregar listas de acuerdos"""

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


class OneListaDeAcuerdoOut(ListaDeAcuerdoOut, OneBaseOut):
    """Esquema para entregar una lista de acuerdo"""
