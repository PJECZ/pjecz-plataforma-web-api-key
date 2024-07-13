"""
Inventarios Equipos, modelos
"""

from datetime import date
from typing import List, Optional

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class InvEquipo(Base, UniversalMixin):
    """InvEquipo"""

    TIPOS = {
        "COMPUTADORA": "COMPUTADORA",
        "LAPTOP": "LAPTOP",
        "IMPRESORA": "IMPRESORA",
        "MULTIFUNCIONAL": "MULTIFUNCIONAL",
        "TELEFONIA": "TELEFONIA",
        "SERVIDOR": "SERVIDOR",
        "SCANNER": "SCANNER",
        "SWITCH": "SWITCH",
        "VIDEOGRABACION": "VIDEOGRABACION",
        "OTROS": "OTROS",
    }

    # Nombre de la tabla
    __tablename__ = "inv_equipos"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    inv_custodia_id: Mapped[int] = mapped_column(ForeignKey("inv_custodias.id"))
    inv_custodia: Mapped["InvCustodia"] = relationship(back_populates="inv_equipos")
    inv_modelo_id: Mapped[int] = mapped_column(ForeignKey("inv_modelos.id"))
    inv_modelo: Mapped["InvModelo"] = relationship(back_populates="inv_equipos")
    inv_red_id: Mapped[int] = mapped_column(ForeignKey("inv_redes.id"))
    inv_red: Mapped["InvRed"] = relationship(back_populates="inv_equipos")

    # Columnas
    fecha_fabricacion: Mapped[Optional[date]]
    numero_serie: Mapped[Optional[str]] = mapped_column(String(256))
    numero_inventario: Mapped[Optional[str]]
    descripcion: Mapped[str] = mapped_column(String(256))
    tipo: Mapped[str] = mapped_column(Enum(*TIPOS, name="tipos", native_enum=False), index=True)
    direccion_ip: Mapped[Optional[str]] = mapped_column(String(256))
    direccion_mac: Mapped[Optional[str]] = mapped_column(String(256))
    numero_nodo: Mapped[Optional[int]]
    numero_switch: Mapped[Optional[int]]
    numero_puerto: Mapped[Optional[int]]

    # Hijos
    inv_componentes: Mapped[List["InvComponente"]] = relationship("InvComponente", back_populates="inv_equipo", lazy="dynamic")

    @property
    def inv_custodia_nombre_completo(self):
        """Nombre completo de la custodia"""
        return self.inv_custodia.nombre_completo

    @property
    def distrito_id(self):
        """Id del distrito"""
        return self.inv_custodia.usuario.oficina.distrito_id

    @property
    def distrito_clave(self):
        """Clave del distrito"""
        return self.inv_custodia.usuario.oficina.distrito.clave

    @property
    def domicilio_edificio(self):
        """Edificio del domicilio"""
        return self.inv_custodia.usuario.oficina.domicilio.edificio

    @property
    def inv_marca_id(self):
        """ID de la marca"""
        return self.inv_modelo.inv_marca_id

    @property
    def inv_marca_nombre(self):
        """Nombre de la marca"""
        return self.inv_modelo.inv_marca.nombre

    @property
    def inv_modelo_descripcion(self):
        """Descripción del modelo"""
        return self.inv_modelo.descripcion

    @property
    def inv_red_nombre(self):
        """Nombre de la red"""
        return self.inv_red.nombre

    @property
    def oficina_id(self):
        """ID de la oficina"""
        return self.inv_custodia.usuario.oficina_id

    @property
    def oficina_clave(self):
        """Clave de la oficina"""
        return self.inv_custodia.usuario.oficina.clave

    @property
    def usuario_id(self):
        """ID del usuario"""
        return self.inv_custodia.usuario_id

    @property
    def usuario_email(self):
        """Email del usuario"""
        return self.inv_custodia.usuario.email

    @property
    def disco_duro(self):
        """Disco duro"""
        for inv_componente in self.inv_componentes:
            if inv_componente.inv_categoria.nombre == "DISCO DURO":
                return f"{inv_componente.descripcion}; {inv_componente.version}"
        return ""

    @property
    def memoria_ram(self):
        """Memoria RAM"""
        for inv_componente in self.inv_componentes:
            if inv_componente.inv_categoria.nombre == "MEMORIA RAM":
                return inv_componente.descripcion
        return ""

    @property
    def procesador(self):
        """Procesador"""
        for inv_componente in self.inv_componentes:
            if inv_componente.inv_categoria.nombre == "PROCESADOR":
                return f"{inv_componente.descripcion}; {inv_componente.generacion}; {inv_componente.version}"
        return ""

    def __repr__(self):
        """Representación"""
        return f"<InvEquipo {self.id}>"
