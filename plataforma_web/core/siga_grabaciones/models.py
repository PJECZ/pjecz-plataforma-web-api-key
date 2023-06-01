"""
SIGA Grabaciones, modelos
"""
from collections import OrderedDict

from sqlalchemy import Column, DateTime, Enum, ForeignKey, JSON, Integer, String, Time
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class SIGAGrabacion(Base, UniversalMixin):
    """SIGAGrabacion"""

    ESTADOS = OrderedDict(
        [
            ("VALIDO", "Válida"),
            ("INVALIDO", "Corrupta en algún tipo de dato"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "siga_grabaciones"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    siga_sala_id = Column(Integer, ForeignKey("siga_salas.id"), index=True, nullable=False)
    siga_sala = relationship("SIGASala", back_populates="siga_grabaciones")
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="siga_grabaciones")
    materia_id = Column(Integer, ForeignKey("materias.id"), index=True, nullable=False)
    materia = relationship("Materia", back_populates="siga_grabaciones")

    # Columnas
    expediente = Column(String(32), nullable=False)
    inicio = Column(DateTime(), nullable=False)
    termino = Column(DateTime())
    archivo_nombre = Column(String(128), nullable=False)
    justicia_ruta = Column(String(512))
    storage_url = Column(String(512))
    tamanio = Column(Integer())
    duracion = Column(Time())
    transcripcion = Column(JSON())
    estado = Column(Enum(*ESTADOS, name="tipos_estados", native_enum=False), index=True, nullable=False)
    nota = Column(String(512))

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

    @property
    def materia_nombre(self):
        """Nombre de la materia"""
        return self.materia.nombre

    @property
    def siga_sala_clave(self):
        """Clave de la sala"""
        return self.siga_sala.clave

    def __repr__(self):
        """Representación"""
        return f"<SIGAGrabacion {self.id}>"
