"""
Oficinas v3, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict, Field

from lib.schemas_base import OneBaseOut


class ItemOficinaOut(BaseModel):
    """Esquema para entregar oficinas"""

    id: int = Field(None)
    distrito_clave: str = Field(None)
    distrito_nombre_corto: str = Field(None)
    domicilio_edificio: str = Field(None)
    clave: str = Field(None)
    descripcion_corta: str = Field(None)
    es_jurisdiccional: bool = Field(None)
    model_config = ConfigDict(from_attributes=True)


class OneOficinaOut(ItemOficinaOut, OneBaseOut):
    """Esquema para entregar una oficina"""

    distrito_id: int = Field(None)
    distrito_nombre: str = Field(None)
    domicilio_id: int = Field(None)
    domicilio_completo: str = Field(None)
    descripcion: str = Field(None)
