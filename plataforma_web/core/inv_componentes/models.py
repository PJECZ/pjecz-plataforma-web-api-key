"""
Inventarios Componentes, modelos
"""

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class InvComponente(Base, UniversalMixin):
    """InvComponente"""

    GENERACIONES = {
        "NO DEFINIDO": "No definido",
        "2da Gen": "Segunda",
        "3er Gen": "Tercera",
        "4ta Gen": "Cuarta",
        "5ta Gen": "Quinta",
        "6ta Gen": "Sexta",
        "7ma Gen": "Septima",
        "8va Gen": "Octava",
        "9na Gen": "Novena",
        "10ma Gen": "Decima",
        "11va Gen": "Onceava",
        "12va Gen": "Doceava",
    }

    # Nombre de la tabla
    __tablename__ = "inv_componentes"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    inv_categoria_id: Mapped[int] = mapped_column(ForeignKey("inv_categorias.id"))
    inv_categoria: Mapped["InvCategoria"] = relationship(back_populates="inv_componentes")
    inv_equipo_id: Mapped[int] = mapped_column(ForeignKey("inv_equipos.id"))
    inv_equipo: Mapped["InvEquipo"] = relationship(back_populates="inv_componentes")

    # Columnas
    descripcion: Mapped[str] = mapped_column(String(256))
    cantidad: Mapped[int]
    generacion: Mapped[str] = mapped_column(Enum(*GENERACIONES, name="generacion", native_enum=False), index=True)
    vesion: Mapped[str] = mapped_column(String(256))

    @property
    def inv_categoria_nombre(self):
        """Nombre de la categoría"""
        return self.inv_categoria.nombre

    @property
    def inv_equipo_descripcion(self):
        """Descripción del equipo"""
        return self.inv_equipo.descripcion

    def __repr__(self):
        """Representación"""
        return f"<InvComponente {self.id}>"
