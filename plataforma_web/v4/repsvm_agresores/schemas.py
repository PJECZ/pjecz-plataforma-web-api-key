"""
REPSVM Agresores v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemRevpsmAgresorOut(BaseModel):
    """Esquema para entregar agresores"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    consecutivo: int = Field(None)
    nombre: str = Field(None)
    numero_causa: str = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneRepsvmAgresorOut(ItemRevpsmAgresorOut, OneBaseOut):
    """Esquema para entregar un agresor"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    delito_generico: str = Field(None)
    delito_especifico: str = Field(None)
    observaciones: str = Field(None)
    pena_impuesta: str = Field(None)
    sentencia_url: str = Field(None)
    tipo_juzgado: str = Field(None)
    tipo_sentencia: str = Field(None)
