"""
Autoridades v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class AutoridadListOut(BaseModel):
    """Esquema para entregar autoridades como listado"""

    id: int | None = None
    clave: str | None = None
    descripcion_corta: str | None = None
    model_config = ConfigDict(from_attributes=True)


class AutoridadOut(AutoridadListOut):
    """Esquema para entregar autoridades como paginado"""

    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    materia_id: int | None = None
    materia_clave: str | None = None
    materia_nombre: str | None = None
    descripcion: str | None = None
    es_cemasc: bool | None = None
    es_defensoria: bool | None = None
    es_extinto: bool | None = None
    es_jurisdiccional: bool | None = None
    es_notaria: bool | None = None
    es_organo_especializado: bool | None = None
    organo_jurisdiccional: str | None = None
    directorio_edictos: str | None = None
    directorio_glosas: str | None = None
    directorio_listas_de_acuerdos: str | None = None
    directorio_sentencias: str | None = None
    audiencia_categoria: str | None = None


class OneAutoridadOut(AutoridadOut, OneBaseOut):
    """Esquema para entregar un autoridad"""
