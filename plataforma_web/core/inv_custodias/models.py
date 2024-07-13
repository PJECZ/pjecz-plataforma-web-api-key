"""
Inventarios Custodias, modelos
"""

from datetime import date
from typing import List

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class InvCustodia(Base, UniversalMixin):
    """InvCustodia"""

    # Nombre de la tabla
    __tablename__ = "inv_custodias"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Clave foránea
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped["Usuario"] = relationship(back_populates="inv_custodias")

    # Columnas
    fecha: Mapped[date] = mapped_column(Date(), index=True)
    curp: Mapped[str] = mapped_column(String(256))
    nombre_completo: Mapped[str] = mapped_column(String(256))

    # Hijos
    inv_equipos: Mapped[List["InvEquipo"]] = relationship("InvEquipo", back_populates="inv_custodia", lazy="dynamic")

    @property
    def distrito_id(self):
        """Id del distrito"""
        return self.usuario.oficina.distrito_id

    @property
    def distrito_clave(self):
        """Clave del distrito"""
        return self.usuario.oficina.distrito.clave

    @property
    def domicilio_edificio(self):
        """Edificio del domicilio"""
        return self.usuario.oficina.domicilio.edificio

    @property
    def oficina_id(self):
        """Id de la oficina"""
        return self.usuario.oficina_id

    @property
    def oficina_clave(self):
        """Clave de la oficina"""
        return self.usuario.oficina.clave

    @property
    def usuario_email(self):
        """Email del usuario"""
        return self.usuario.email

    def __repr__(self):
        """Representación"""
        return f"<InvCustodia {self.id}>"
