"""
Inventarios Equipos v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class InvEquipoOut(BaseModel):
    """Esquema para entregar equipos"""

    id: int | None
    creado: datetime | None
    descripcion: str | None
    direccion_ip: str | None
    direccion_mac: str | None
    disco_duro: str | None
    distrito_id: int | None
    distrito_clave: str | None
    domicilio_edificio: str | None
    fecha_fabricacion: date | None
    inv_custodia_id: int | None
    inv_custodia_nombre_completo: str | None
    inv_marca_id: int | None
    inv_marca_nombre: str | None
    inv_modelo_id: int | None
    inv_modelo_descripcion: str | None
    inv_red_id: int | None
    inv_red_nombre: str | None
    memoria_ram: str | None
    numero_serie: str | None
    numero_inventario: int | None
    numero_nodo: int | None
    numero_switch: int | None
    numero_puerto: int | None
    oficina_id: int | None
    oficina_clave: str | None
    procesador: str | None
    tipo: str | None
    usuario_id: int | None
    usuario_email: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneInvEquipoOut(InvEquipoOut, OneBaseOut):
    """Esquema para entregar un equipo"""
