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
            ("PENDIENTE", "Pendiente"),  # El SOLICITANTE comienza una solicitud de Remesa
            ("CANCELADO", "Cancelado"),  # El SOLICITANTE se arrepiente de crear una Remesa
            ("ENVIADO", "Enviado"),  # El SOLICITANTE pide que recojan la remesa. El JEFE_REMESA ve el pedido
            ("RECHAZADO", "Rechazado"),  # El JEFE_REMESA rechaza la remesa
            ("ASIGNADO", "Asignado"),  # El JEFE_REMESA acepta la remesa y la asigna a un ARCHIVISTA
            ("ARCHIVADO", "Archivado"),  # El ARCHIVISTA termina de procesar la remesa
            ("ARCHIVADO CON ANOMALIA", "Archivado con Anomalía"),  # El ARCHIVISTA termina de procesar la remesa pero almenos un documento presentó anomalía
        ]
    )

    TIPOS_DOCUMENTOS = OrderedDict(
        [
            ("CUADERNILLO", "Cuadernillo"),
            ("ENCOMIENDA", "Encomienda"),
            ("EXHORTO", "Exhorto"),
            ("EXPEDIENTE", "Expediente"),
            ("EXPEDIENTILLO", "Expedientillo"),
            ("FOLIO", "Folio"),
            ("LIBRO", "Libro"),
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
    usuario_asignado_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    usuario_asignado = relationship("Usuario", back_populates="arc_remesas_asignadas")

    # Columnas
    anio = Column(Integer, nullable=False)
    esta_archivado = Column(Boolean, nullable=False, default=False)
    num_oficio = Column(String(16))
    rechazo = Column(String(256))
    observaciones = Column(String(256))
    tiempo_enviado = Column(DateTime)
    tipo_documentos = Column(
        Enum(*TIPOS_DOCUMENTOS, name="tipos", native_enum=False),
        index=True,
        nullable=False,
    )
    num_documentos = Column(Integer, nullable=False)
    num_anomalias = Column(Integer, nullable=False)
    razon = Column(Enum(*RAZONES, name="razones", native_enum=False))
    estado = Column(
        Enum(*ESTADOS, name="estados", native_enum=False),
        nullable=False,
    )

    # Hijos
    arc_remesas_documentos = relationship("ArcRemesaDocumento", back_populates="arc_remesa")

    def __repr__(self):
        """Representación"""
        return f"<ArcRemesa {self.id}>"
