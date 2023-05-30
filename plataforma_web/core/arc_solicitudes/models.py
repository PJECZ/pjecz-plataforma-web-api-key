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
        index=True,
        nullable=False,
    )
    razon = Column(
        Enum(*RAZONES, name="razon", native_enum=False),
        index=True,
        nullable=False,
    )
    observaciones_solicitud = Column(String(256))
    observaciones_razon = Column(String(256))

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
    def usuario_asignado_email(self):
        """Email del usuario"""
        return self.usuario_asignado.email

    @property
    def usuario_asignado_nombre(self):
        """Nombre del usuario"""
        return self.usuario_asignado.nombre

    def __repr__(self):
        """Representación"""
        return f"<ArcSolicitud {self.id}>"
