"""
Epocas, modelos
"""

from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Epoca(Base, UniversalMixin):
    """Epoca"""

    # Nombre de la tabla
    __tablename__ = "epocas"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Columnas
    nombre: Mapped[str] = mapped_column(String(256), unique=True)

    # Hijos
    tesis_jurisprudencias: Mapped[List["TesisJurisprudencia"]] = relationship("TesisJurisprudencia", back_populates="epoca")

    def __repr__(self):
        """Representación"""
        return f"<Epoca {self.id}>"
