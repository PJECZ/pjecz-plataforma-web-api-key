"""
Archivo - Juzgados Extintos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ArcJuzgadoExtintoListOut(BaseModel):
    """Esquema para entregar juzgados extintos como listado"""

    id: int | None = None
    clave: str | None = None
    descripcion_corta: str | None = None
    model_config = ConfigDict(from_attributes=True)


class ArcJuzgadoExtintoOut(ArcJuzgadoExtintoListOut):
    """Esquema para entregar juzgados extintos como paginado"""

    descripcion: str | None = None


class OneArcJuzgadoExtintoOut(ArcJuzgadoExtintoOut, OneBaseOut):
    """Esquema para entregar un juzgado extinto"""
