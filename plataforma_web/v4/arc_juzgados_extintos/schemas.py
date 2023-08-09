"""
Archivo - Juzgados Extintos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcJuzgadoExtintoListOut(BaseModel):
    """Esquema para entregar juzgados extintos como listado"""

    id: int | None
    clave: str | None
    descripcion_corta: str | None
    model_config = ConfigDict(from_attributes=True)


class ArcJuzgadoExtintoOut(ArcJuzgadoExtintoListOut):
    """Esquema para entregar juzgados extintos como paginado"""

    descripcion: str | None


class OneArcJuzgadoExtintoOut(ArcJuzgadoExtintoOut, OneBaseOut):
    """Esquema para entregar un juzgado extinto"""
