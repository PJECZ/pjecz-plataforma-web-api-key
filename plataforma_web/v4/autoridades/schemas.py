"""
Autoridades v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemAutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    clave: str = Field(None)
    descripcion_corta: str = Field(None)
    materia_clave: str = Field(None)
    materia_nombre: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneAutoridadOut(ItemAutoridadOut, OneBaseOut):
    """Esquema para entregar una autoridad"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    materia_id: int = Field(None)
    descripcion: str = Field(None)
    es_cemasc: bool = Field(None)
    es_defensoria: bool = Field(None)
    es_extinto: bool = Field(None)
    es_jurisdiccional: bool = Field(None)
    es_notaria: bool = Field(None)
    es_organo_especializado: bool = Field(None)
    organo_jurisdiccional: str = Field(None)
    directorio_edictos: str = Field(None)
    directorio_glosas: str = Field(None)
    directorio_listas_de_acuerdos: str = Field(None)
    directorio_sentencias: str = Field(None)
    audiencia_categoria: str = Field(None)
