"""
SIGA Grabaciones v3, esquemas de pydantic
"""
from datetime import datetime, timedelta

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class SIGAGrabacionIn(BaseModel):
    """Esquema para recibir una grabacion"""

    autoridad_clave: str | None = None
    siga_sala_clave: str | None = None
    materia_clave: str | None = None
    expediente: str | None = None
    inicio: datetime | None = None
    termino: datetime | None = None
    archivo_nombre: str | None = None
    justicia_ruta: str | None = None
    tamanio: int | None = None
    duracion: timedelta | None = None
    estado: str | None = None


class SIGAGrabacionOut(SIGAGrabacionIn):
    """Esquema para entregar grabaciones"""

    id: int | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    distrito_nombre: str | None = None
    distrito_nombre_corto: str | None = None
    autoridad_id: int | None = None
    autoridad_descripcion: str | None = None
    autoridad_descripcion_corta: str | None = None
    siga_sala_id: int | None = None
    materia_id: int | None = None
    materia_nombre: str | None = None
    storage_url: str | None = None
    transcripcion: dict | None = None
    nota: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneSIGAGrabacionOut(SIGAGrabacionOut, OneBaseOut):
    """Esquema para entregar una grabacion"""
