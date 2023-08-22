"""
Inventarios Equipos v3, esquemas de pydantic
"""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class InvEquipoOut(BaseModel):
    """Esquema para entregar equipos"""

    id: int | None = None
    creado: datetime | None = None
    descripcion: str | None = None
    direccion_ip: str | None = None
    direccion_mac: str | None = None
    disco_duro: str | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    domicilio_edificio: str | None = None
    fecha_fabricacion: date | None = None
    inv_custodia_id: int | None = None
    inv_custodia_nombre_completo: str | None = None
    inv_marca_id: int | None = None
    inv_marca_nombre: str | None = None
    inv_modelo_id: int | None = None
    inv_modelo_descripcion: str | None = None
    inv_red_id: int | None = None
    inv_red_nombre: str | None = None
    memoria_ram: str | None = None
    numero_serie: str | None = None
    numero_inventario: int | None = None
    numero_nodo: int | None = None
    numero_switch: int | None = None
    numero_puerto: int | None = None
    oficina_id: int | None = None
    oficina_clave: str | None = None
    procesador: str | None = None
    tipo: str | None = None
    usuario_id: int | None = None
    usuario_email: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneInvEquipoOut(InvEquipoOut, OneBaseOut):
    """Esquema para entregar un equipo"""
