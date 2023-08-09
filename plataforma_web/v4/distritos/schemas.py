"""
Distritos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class DistritoListOut(BaseModel):
    """Esquema para entregar distritos en listado"""

    id: int | None
    clave: str | None
    nombre_corto: str | None
    model_config = ConfigDict(from_attributes=True)


class DistritoOut(DistritoListOut):
    """Esquema para entregar distritos en paginado"""

    nombre: str | None
    es_distrito_judicial: bool | None
    es_distrito: bool | None
    es_jurisdiccional: bool | None


class OneDistritoOut(DistritoOut, OneBaseOut):
    """Esquema para entregar un distrito"""
