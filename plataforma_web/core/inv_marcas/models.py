"""
Inventarios Marcas, modelos
"""

from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class InvMarca(Base, UniversalMixin):
    """InvMarca"""

    # Nombre de la tabla
    __tablename__ = "inv_marcas"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Columnas
    nombre: Mapped[str] = mapped_column(String(256), unique=True)

    # Hijos
    inv_modelos: Mapped[List["InvModelo"]] = relationship("InvModelo", back_populates="inv_marca", lazy="dynamic")

    def __repr__(self):
        """Representación"""
        return f"<InvMarca {self.id}>"
