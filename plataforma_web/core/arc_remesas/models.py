"""
Archivo - Remesas, modelos
"""
from collections import OrderedDict

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ArcRemesa(Base, UniversalMixin):
    """ArcRemesa"""

    ESTADOS = OrderedDict(
        [
            ("PENDIENTE", "Pendiente"),
            ("CANCELADO", "Cancelado"),
            ("ENVIADO", "Enviado"),
            ("RECHAZADO", "Rechazado"),
            ("ASIGNADO", "Asignado"),
            ("ARCHIVADO", "Archivado"),
            ("ARCHIVADO CON ANOMALIA", "Archivado con Anomalía"),
        ]
    )

    RAZONES = OrderedDict(
        [
            ("SIN ORDEN CRONOLÓGICO", "Sin orden cronológico."),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "arc_remesas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="arc_remesas")
    usuario_asignado_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=True)  # Puede ser NULL
    usuario_asignado = relationship("Usuario", back_populates="arc_remesas_asignadas")

    # Columnas
    anio = Column(String(16), nullable=False)
    esta_archivado = Column(Boolean, nullable=False, default=False)
    num_oficio = Column(String(16))
    rechazo = Column(String(256))
    tiempo_enviado = Column(DateTime)
    num_documentos = Column(Integer, nullable=False)
    num_anomalias = Column(Integer, nullable=False)
    razon = Column(Enum(*RAZONES, name="razones", native_enum=False), index=True, nullable=False)
    estado = Column(Enum(*ESTADOS, name="estados", native_enum=False), index=True, nullable=False)

    # Hijos
    arc_remesas_documentos = relationship("ArcRemesaDocumento", back_populates="arc_remesa")

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
    def usuario_asignado_email(self):
        """Email del usuario"""
        return self.usuario_asignado.email if self.usuario_asignado else None

    @property
    def usuario_asignado_nombre(self):
        """Nombre del usuario"""
        return self.usuario_asignado.nombre if self.usuario_asignado else None

    def __repr__(self):
        """Representación"""
        return f"<ArcRemesa {self.id}>"
