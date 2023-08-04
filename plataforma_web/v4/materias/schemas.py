"""
Materias v3, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class MateriaOut(BaseModel):
    """Esquema para entregar materias"""

    id: int | None
    clave: str | None
    nombre: str | None
    model_config = ConfigDict(from_attributes=True)


class OneMateriaOut(MateriaOut, OneBaseOut):
    """Esquema para entregar una materia"""
