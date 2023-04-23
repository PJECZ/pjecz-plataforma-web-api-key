"""
Peritos v3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class PeritoOut(BaseModel):
    """Esquema para entregar peritos"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    perito_tipo_id: int | None
    perito_tipo_nombre: str | None
    nombre: str | None
    domicilio: str | None
    telefono_fijo: str | None
    telefono_celular: str | None
    email: str | None
    notas: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OnePeritoOut(PeritoOut, OneBaseOut):
    """Esquema para entregar un perito"""
