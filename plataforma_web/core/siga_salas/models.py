"""
SIGA Salas, modelos
"""
from collections import OrderedDict

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class SIGASala(Base, UniversalMixin):
    """SIGASala"""

    ESTADOS = OrderedDict(
        [
            ("OPERATIVO", "Operativo"),
            ("FUERA DE LINEA", "Fuera de línea"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "siga_salas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    domicilio_id = Column(Integer, ForeignKey("domicilios.id"), index=True, nullable=False)
    domicilio = relationship("Domicilio", back_populates="siga_salas")

    # Columnas
    clave = Column(String(16), unique=True, nullable=False)
    direccion_ip = Column(String(16))
    direccion_nvr = Column(String(16))
    estado = Column(Enum(*ESTADOS, name="tipos_estados", native_enum=False), index=True, nullable=False)
    descripcion = Column(String(1024))

    # Hijos
    siga_bitacoras = relationship("SIGABitacora", back_populates="siga_sala")
    siga_grabaciones = relationship("SIGAGrabacion", back_populates="siga_sala")

    @property
    def domicilio_completo(self):
        """Domicilio completo de la oficina"""
        return self.domicilio.completo

    @property
    def domicilio_edificio(self):
        """Edificio del domicilio"""
        return self.domicilio.edificio

    def __repr__(self):
        """Representación"""
        return f"<SIGASala {self.id}>"
