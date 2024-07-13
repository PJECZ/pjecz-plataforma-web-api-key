"""
Centros de Trabajo, modelos
"""

from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class CentroTrabajo(Base, UniversalMixin):
    """CentroTrabajo"""

    # Nombre de la tabla
    __tablename__ = "centros_trabajos"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    distrito_id: Mapped[int] = mapped_column(ForeignKey("distritos.id"))
    distrito: Mapped["Distrito"] = relationship(back_populates="centros_trabajos")
    domicilio_id: Mapped[int] = mapped_column(ForeignKey("domicilios.id"))
    domicilio: Mapped["Domicilio"] = relationship(back_populates="centros_trabajos")

    # Columnas
    clave: Mapped[str] = mapped_column(String(16), unique=True)
    nombre: Mapped[str] = mapped_column(String(256))
    telefono: Mapped[str] = mapped_column(String(48))

    # Hijos
    funcionarios: Mapped[List["Funcionario"]] = relationship("Funcionario", back_populates="centro_trabajo")

    @property
    def distrito_clave(self):
        """Clave del distrito"""
        return self.distrito.clave

    @property
    def distrito_nombre(self):
        """Nombre del distrito"""
        return self.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Nombre corto del distrito"""
        return self.distrito.nombre_corto

    @property
    def domicilio_completo(self):
        """Domicilio completo de la oficina"""
        return self.domicilio.completo

    @property
    def domicilio_edificio(self):
        """Edificio de la oficina"""
        return self.domicilio.edificio

    def __repr__(self):
        """Representación"""
        return f"<CentroTrabajo {self.clave}>"
