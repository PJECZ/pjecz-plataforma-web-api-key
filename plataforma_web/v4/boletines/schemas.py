"""
Boletines v3, esquemas de pydantic
"""
from datetime import datetime
from typing import Dict

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class BoletinIn(BaseModel):
    """Esquema para recibir un boletin"""

    asunto: str | None
    contenido: Dict | None
    estado: str | None
    envio_programado: datetime | None
    puntero: int | None
    termino_programado: datetime | None


class BoletinOut(BoletinIn):
    """Esquema para entregar boletines"""

    id: int | None
    model_config = ConfigDict(from_attributes=True)


class OneBoletinOut(BoletinOut, OneBaseOut):
    """Esquema para entregar un boletin"""
