"""
REPSVM Agresores v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class RepsvmAgresorOut(BaseModel):
    """Esquema para entregar agresores"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    consecutivo: int | None
    delito_generico: str | None
    delito_especifico: str | None
    nombre: str | None
    numero_causa: str | None
    pena_impuesta: str | None
    observaciones: str | None
    sentencia_url: str | None
    tipo_juzgado: str | None
    tipo_sentencia: str | None
    model_config = ConfigDict(from_attributes=True)


class OneRepsvmAgresorOut(RepsvmAgresorOut, OneBaseOut):
    """Esquema para entregar un agresor"""
