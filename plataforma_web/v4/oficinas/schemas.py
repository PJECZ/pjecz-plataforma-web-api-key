"""
Oficinas v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class OficinaListOut(BaseModel):
    """Esquema para entregar oficinas"""

    id: int | None
    clave: str | None
    descripcion_corta: str | None
    model_config = ConfigDict(from_attributes=True)


class OficinaOut(OficinaListOut):
    """Esquema para entregar oficinas"""

    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    domicilio_id: int | None
    domicilio_completo: str | None
    domicilio_edificio: str | None
    descripcion: str | None
    es_jurisdiccional: bool | None


class OneOficinaOut(OficinaOut, OneBaseOut):
    """Esquema para entregar un oficina"""
