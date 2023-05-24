"""
Inventarios Custodias v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class InvCustodiaOut(BaseModel):
    """Esquema para entregar custodias"""

    id: int | None
    creado: datetime | None
    curp: str | None
    distrito_id: int | None
    distrito_clave: str | None
    fecha: date | None
    nombre_completo: str | None
    oficina_id: int | None
    oficina_clave: str | None
    usuario_id: int | None
    usuario_email: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneInvCustodiaOut(InvCustodiaOut, OneBaseOut):
    """Esquema para entregar un custodia"""
