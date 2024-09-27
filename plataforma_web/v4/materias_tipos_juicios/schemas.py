"""
Materias-Tipos de Juicios v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemMateriaTipoJuicioOut(BaseModel):
    """Esquema para entregar materias-tipos de juicios"""

    id: int = Field(None)
    materia_clave: str = Field(None)
    materia_nombre: str = Field(None)
    descripcion: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneMateriaTipoJuicioOut(ItemMateriaTipoJuicioOut, OneBaseOut):
    """Esquema para entregar un materia-tipo de juicio"""

    materia_id: int = Field(None)
