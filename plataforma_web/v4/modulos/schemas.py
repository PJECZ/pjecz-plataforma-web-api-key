"""
Modulos v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class ModuloListOut(BaseModel):
    """Esquema para entregar modulos"""

    id: int | None
    nombre_corto: str | None
    model_config = ConfigDict(from_attributes=True)


class ModuloOut(ModuloListOut):
    """Esquema para entregar modulos"""

    nombre: str | None
    icono: str | None
    ruta: str | None
    en_navegacion: bool | None


class OneModuloOut(ModuloOut, OneBaseOut):
    """Esquema para entregar un modulo"""
