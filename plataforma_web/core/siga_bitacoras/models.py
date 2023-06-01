"""
SIGA Bitacoras, modelos
"""
from collections import OrderedDict

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class SIGABitacora(Base, UniversalMixin):
    """SIGABitacora"""

    ESTADOS = OrderedDict(
        [
            ("PENDIENTE", "Operación pendiente de realizar"),
            ("CORRECTO", "Operación terminada con éxito"),
            ("CANCELADO", "Operación cancelada"),
            ("ERROR", "Operación con error"),
        ]
    )

    ACCIONES = OrderedDict(
        [
            ("LEER NOMBRE", "Leer el nombre del archivo"),
            ("INSERT", "Crear nuevo registro en la tabla"),
            ("UPLOAD", "Copiar el archivo a GDrive"),
            ("METADATOS", "Lectura de metadatos del archivo"),
            ("UPDATE", "Se actualizó el registro"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "siga_bitacoras"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    siga_sala_id = Column(Integer, ForeignKey("siga_salas.id"), index=True, nullable=False)
    siga_sala = relationship("SIGASala", back_populates="siga_bitacoras")

    # Columnas
    accion = Column(Enum(*ACCIONES, name="tipos_acciones", native_enum=False), index=True, nullable=False)
    estado = Column(Enum(*ESTADOS, name="tipos_estados", native_enum=False), index=True, nullable=False)
    descripcion = Column(String(512))

    @property
    def siga_sala_clave(self):
        """Clave de la sala"""
        return self.siga_sala.clave

    def __repr__(self):
        """Representación"""
        return f"<SIGABitacora {self.id}>"
