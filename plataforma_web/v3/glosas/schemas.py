"""
Glosas v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class GlosaIn(BaseModel):
    """Esquema para recibir una glosa"""

    autoridad_id: int | None
    fecha: date | None
    tipo_juicio: str | None
    descripcion: str | None
    expediente: str | None
    archivo: str | None
    url: str | None


class GlosaOut(GlosaIn):
    """Esquema para entregar glosas"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_clave: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneGlosaOut(GlosaOut, OneBaseOut):
    """Esquema para entregar una glosa"""
