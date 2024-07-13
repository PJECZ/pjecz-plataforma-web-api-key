"""
Bitacoras, modelos
"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Bitacora(Base, UniversalMixin):
    """Bitacora"""

    # Nombre de la tabla
    __tablename__ = "bitacoras"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    modulo_id: Mapped[int] = mapped_column(ForeignKey("modulos.id"))
    modulo: Mapped["Modulo"] = relationship(back_populates="bitacoras")
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped["Usuario"] = relationship(back_populates="bitacoras")

    # Columnas
    descripcion: Mapped[str] = mapped_column(String(256))
    url: Mapped[str] = mapped_column(String(512))

    @property
    def modulo_nombre(self):
        """Nombre del modulo"""
        return self.modulo.nombre

    @property
    def usuario_email(self):
        """email del usuario"""
        return self.usuario.email

    @property
    def usuario_nombre(self):
        """Nombre del usuario"""
        return self.usuario.nombre

    def __repr__(self):
        """Representación"""
        return f"<Bitacora {self.id}>"
