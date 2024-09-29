"""
Autoridades v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemAutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    id: int = Field(None)
    clave: str = Field(None)
    descripcion: str = Field(None)
    descripcion_corta: str = Field(None)
    es_cemasc: bool = Field(None)
    es_creador_glosas: bool = Field(None)
    es_defensoria: bool = Field(None)
    es_jurisdiccional: bool = Field(None)
    es_notaria: bool = Field(None)
    es_organo_especializado: bool = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneAutoridadOut(ItemAutoridadOut, OneBaseOut):
    """Esquema para entregar una autoridad"""

    distrito_id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    distrito_nombre: str = Field(None)
    materia_id: int = Field(None)
    materia_clave: str = Field(None)
    materia_nombre: str = Field(None)
    organo_jurisdiccional: str = Field(None)
    audiencia_categoria: str = Field(None)
