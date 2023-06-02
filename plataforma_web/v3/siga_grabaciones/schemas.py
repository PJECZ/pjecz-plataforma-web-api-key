"""
SIGA Grabaciones v3, esquemas de pydantic
"""
from datetime import datetime, time

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class SIGAGrabacionIn(BaseModel):
    """Esquema para recibir una grabacion"""

    autoridad_id: int | None
    autoridad_clave: str | None
    siga_sala_id: int | None
    siga_sala_clave: str | None
    materia_id: int | None
    materia_clave: str | None
    expediente: str | None
    inicio: datetime | None
    termino: datetime | None
    archivo_nombre: str | None
    justicia_ruta: str | None
    storage_url: str | None
    tamanio: int | None
    duracion: time | None


class SIGAGrabacionOut(SIGAGrabacionIn):
    """Esquema para entregar grabaciones"""

    id: int | None
    distrito_id: int | None
    distrito_clave: str | None
    distrito_nombre: str | None
    distrito_nombre_corto: str | None
    autoridad_descripcion: str | None
    autoridad_descripcion_corta: str | None
    materia_nombre: str | None
    transcripcion: dict | None
    estado: str | None
    nota: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneSIGAGrabacionOut(SIGAGrabacionOut, OneBaseOut):
    """Esquema para entregar una grabacion"""
