"""
Ubicaciones de Expedientes, modelos
"""

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class UbicacionExpediente(Base, UniversalMixin):
    """UbicacionExpediente"""

    UBICACIONES = {
        "NO DEFINIDO": "No Definido",
        "ARCHIVO": "Archivo",
        "JUZGADO": "Juzgado",
        "REMESA": "Remesa",
    }

    # Nombre de la tabla
    __tablename__ = "ubicaciones_expedientes"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    autoridad_id: Mapped[int] = mapped_column(ForeignKey("autoridades.id"))
    autoridad: Mapped["Autoridad"] = relationship(back_populates="ubicaciones_expedientes")

    # Columnas
    expediente: Mapped[str] = mapped_column(String(256))
    ubicacion: Mapped[str] = mapped_column(Enum(*UBICACIONES, name="ubicaciones_opciones", native_enum=False), index=True)

    @property
    def distrito_id(self):
        """Distrito ID"""
        return self.autoridad.distrito_id

    @property
    def distrito_clave(self):
        """Distrito clave"""
        return self.autoridad.distrito.clave

    @property
    def distrito_nombre(self):
        """Distrito nombre"""
        return self.autoridad.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Distrito nombre corto"""
        return self.autoridad.distrito.nombre_corto

    @property
    def autoridad_clave(self):
        """Autoridad clave"""
        return self.autoridad.clave

    @property
    def autoridad_descripcion(self):
        """Autoridad descripción"""
        return self.autoridad.descripcion

    @property
    def autoridad_descripcion_corta(self):
        """Autoridad descripción corta"""
        return self.autoridad.descripcion_corta

    def __repr__(self):
        """Representación"""
        return f"<UbicacionExpediente {self.id}>"
