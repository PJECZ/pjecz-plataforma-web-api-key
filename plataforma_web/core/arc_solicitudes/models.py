"""
Archivo - Solicitudes, modelos
"""
from collections import OrderedDict

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ArcSolicitud(Base, UniversalMixin):
    """ArcSolicitud"""

    ESTADOS = OrderedDict(
        [
            ("SOLICITADO", "Solicitado"),
            ("CANCELADO", "Cancelado"),
            ("ASIGNADO", "Asignado"),
            ("ENCONTRADO", "Encontrado"),
            ("NO ENCONTRADO", "No Encontrado"),
            ("ENVIANDO", "Enviando"),
            ("ENTREGADO", "Entregado"),
        ]
    )

    RAZONES = OrderedDict(
        [
            ("FALTA DE ORIGEN", "Falta de Origen"),
            ("NO COINCIDEN LAS PARTES", "No coinciden las partes"),
            ("PRESTADO", "Prestado"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "arc_solicitudes"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    arc_documento_id = Column(Integer, ForeignKey("arc_documentos.id"), index=True, nullable=False)
    arc_documento = relationship("ArcDocumento", back_populates="arc_solicitudes")
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="arc_solicitudes")
    usuario_asignado_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    usuario_asignado = relationship("Usuario", back_populates="arc_solicitudes_asignadas")

    # Columnas
    usuario_receptor_id = Column(Integer())
    esta_archivado = Column(Boolean, nullable=False, default=False)
    num_folio = Column(String(16))
    tiempo_recepcion = Column(DateTime())
    fojas = Column(Integer())
    estado = Column(
        Enum(*ESTADOS, name="estados", native_enum=False),
        nullable=False,
    )
    razon = Column(Enum(*RAZONES, name="razon", native_enum=False))
    observaciones_solicitud = Column(String(256))
    observaciones_razon = Column(String(256))

    def __repr__(self):
        """Representación"""
        return f"<ArcSolicitud {self.id}>"
