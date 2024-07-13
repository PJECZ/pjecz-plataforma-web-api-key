"""
Domicilios, modelos
"""

from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Domicilio(Base, UniversalMixin):
    """Domicilio"""

    # Nombre de la tabla
    __tablename__ = "domicilios"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    distrito_id: Mapped[int] = mapped_column(ForeignKey("distritos.id"))
    distrito: Mapped["Distrito"] = relationship(back_populates="domicilios")

    # Columnas
    edificio: Mapped[str] = mapped_column(String(64), unique=True)
    estado: Mapped[str] = mapped_column(String(64))
    municipio: Mapped[str] = mapped_column(String(64))
    calle: Mapped[str] = mapped_column(String(256))
    num_ext: Mapped[str] = mapped_column(String(24))
    num_int: Mapped[str] = mapped_column(String(24))
    colonia: Mapped[str] = mapped_column(String(256))
    cp: Mapped[int]
    completo: Mapped[str] = mapped_column(String(1024))
    numeracion_telefonica: Mapped[str] = mapped_column(String(256))

    # Hijos
    centros_trabajos: Mapped[List["CentroTrabajo"]] = relationship("CentroTrabajo", back_populates="domicilio")
    oficinas: Mapped[List["Oficina"]] = relationship("Oficina", back_populates="domicilio")

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

    def __repr__(self):
        """Representación"""
        return f"<Domicilio {self.edificio}>"
