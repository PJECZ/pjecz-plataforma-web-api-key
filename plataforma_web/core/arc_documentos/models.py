"""
Archivo - Documentos, modelos
"""
from collections import OrderedDict

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ArcDocumento(Base, UniversalMixin):
    """ArcDocumento"""

    UBICACIONES = OrderedDict(
        [
            ("NO DEFINIDO", "No Definido"),
            ("ARCHIVO", "Archivo"),
            ("JUZGADO", "Juzgado"),
            ("REMESA", "Remesa"),
        ]
    )

    TIPO_JUZGADOS = OrderedDict(
        [
            ("ORAL", "Oral"),
            ("TRADICIONAL", "Tradicional"),
        ]
    )

    TIPOS = OrderedDict(
        [
            ("NO DEFINIDO", "No Definido"),
            ("CUADERNILLO", "Cuadernillo"),
            ("ENCOMIENDA", "Encomienda"),
            ("EXHORTO", "Exhorto"),
            ("EXPEDIENTE", "Expediente"),
            ("EXPEDIENTILLO", "Expedientillo"),
            ("FOLIO", "Folio"),
            ("LIBRO", "Libro"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "arc_documentos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="arc_documentos")
    arc_juzgado_origen_id = Column(Integer, ForeignKey("arc_juzgados_extintos.id"), index=True, nullable=False)
    arc_juzgado_origen = relationship("ArcJuzgadoExtinto", back_populates="arc_documentos")

    # Columnas
    actor = Column(String(256), nullable=False)
    anio = Column(Integer, nullable=False)
    demandado = Column(String(256))
    expediente = Column(String(16), index=True, nullable=False)
    juicio = Column(String(128))
    fojas = Column(Integer, nullable=False)
    tipo_juzgado = Column(
        Enum(*TIPO_JUZGADOS, name="tipo_juzgados", native_enum=False),
        nullable=False,
    )
    ubicacion = Column(
        Enum(*UBICACIONES, name="ubicaciones", native_enum=False),
        nullable=False,
        default="NO DEFINIDO",
        server_default="NO DEFINIDO",
    )
    tipo = Column(
        Enum(*TIPOS, name="tipos", native_enum=False),
        index=True,
        nullable=False,
        default="NO DEFINIDO",
        server_default="NO DEFINIDO",
    )

    # Hijos
    arc_solicitudes = relationship("ArcSolicitud", back_populates="arc_documento")
    arc_remesas_documentos = relationship("ArcRemesaDocumento", back_populates="arc_documento")

    def __repr__(self):
        """Representación"""
        return f"<ArcDocumento {self.id}>"
