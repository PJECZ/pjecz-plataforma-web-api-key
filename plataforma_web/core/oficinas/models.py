"""
Oficinas, modelos
"""

from datetime import time
from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Oficina(Base, UniversalMixin):
    """Oficina"""

    TIPOS = {
        "NO DEFINIDO": "NO DEFINIDO",
        "O.J. DE 1RA. INSTANCIA": "O.J. DE 1RA. INSTANCIA",
        "O.J. DE 2DA. INSTANCIA": "O.J. DE 2DA. INSTANCIA",
        "ADMINISTRATICO Y/O U. ADMIN.": "ADMINISTRATICO Y/O U. ADMIN.",
    }

    # Nombre de la tabla
    __tablename__ = "oficinas"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    distrito_id: Mapped[int] = mapped_column(ForeignKey("distritos.id"))
    distrito: Mapped["Distrito"] = relationship(back_populates="oficinas")
    domicilio_id: Mapped[int] = mapped_column(ForeignKey("domicilios.id"))
    domicilio: Mapped["Domicilio"] = relationship(back_populates="oficinas")

    # Columnas
    clave: Mapped[str] = mapped_column(String(32), unique=True)
    descripcion: Mapped[str] = mapped_column(String(512))
    descripcion_corta: Mapped[str] = mapped_column(String(64))
    es_jurisdiccional: Mapped[bool] = mapped_column(default=False)
    apertura: Mapped[time]
    cierre: Mapped[time]
    limite_personas: Mapped[int]

    # Hijos
    usuarios: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="oficina")

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
        return f"<Oficina {self.clave}>"
