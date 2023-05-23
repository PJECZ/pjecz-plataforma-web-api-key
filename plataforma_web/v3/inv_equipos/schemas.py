"""
Inventarios Equipos v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class InvEquipoOut(BaseModel):
    """Esquema para entregar equipos"""

    id: int | None
    usuario_id: int | None
    usuario_email: str | None
    usuario_nombre: str | None
    fecha: date | None
    curp: str | None
    nombre_completo: str | None
    creado: datetime | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneInvEquipoOut(InvEquipoOut, OneBaseOut):
    """Esquema para entregar un equipo"""
