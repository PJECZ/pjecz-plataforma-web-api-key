"""
Archivo - Juzgados Extintos, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ArcJuzgadoExtinto(Base, UniversalMixin):
    """ArcJuzgadoExtinto"""

    # Nombre de la tabla
    __tablename__ = "arc_juzgados_extintos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    clave = Column(String(16), nullable=False, unique=True)
    descripcion = Column(String(256), nullable=False)
    descripcion_corta = Column(String(64), nullable=False)

    # Hijos
    arc_documentos = relationship("ArcDocumento", back_populates="arc_juzgado_origen")

    def __repr__(self):
        """Representación"""
        return f"<ArcJuzgadoExtinto {self.clave}>"
