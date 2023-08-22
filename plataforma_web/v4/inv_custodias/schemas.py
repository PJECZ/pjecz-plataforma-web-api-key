"""
Inventarios Custodias v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvCustodiaOut(BaseModel):
    """Esquema para entregar custodias"""

    id: int | None = None
    creado: datetime | None = None
    curp: str | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    domicilio_edificio: str | None = None
    fecha: date | None = None
    nombre_completo: str | None = None
    oficina_id: int | None = None
    oficina_clave: str | None = None
    usuario_id: int | None = None
    usuario_email: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneInvCustodiaOut(InvCustodiaOut, OneBaseOut):
    """Esquema para entregar un custodia"""
