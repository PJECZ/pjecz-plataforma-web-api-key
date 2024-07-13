"""
Inventarios Categorias, modelos
"""

from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class InvCategoria(Base, UniversalMixin):
    """InvCategoria"""

    # Nombre de la tabla
    __tablename__ = "inv_categorias"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Columnas
    nombre: Mapped[str] = mapped_column(String(256), unique=True)

    # Hijos
    inv_componentes: Mapped[List["InvComponente"]] = relationship(
        "InvComponente", back_populates="inv_categoria", lazy="dynamic"
    )

    def __repr__(self):
        """Representación"""
        return f"<InvCategoria {self.nombre}>"
