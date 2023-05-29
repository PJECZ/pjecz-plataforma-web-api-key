"""
Archivo - Remesas Documentos, modelos
"""
from collections import OrderedDict

from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ArcRemesaDocumento(Base, UniversalMixin):
    """ArcRemesaDocumento"""

    TIPOS = OrderedDict(
        [
            ("TRADICIONAL", "Pendiente"),
            ("ORAL", "Cancelado"),
        ]
    )

    ANOMALIAS = OrderedDict(
        [
            ("EXPEDIENTE CON NUMERO INCORRECTO", "Expediente con número incorrecto"),
            ("EXPEDIENTE CON ANO INCORRECTO", "Expediente con año incorrecto"),
            ("EXPEDIENTE ENLISTADO Y NO ENVIADO", "Expediente enlistado y no enviado"),
            ("EXPEDIENTE CON PARTES INCORRECTAS", "Expediente con partes incorrectas"),
            ("EXPEDIENTE SIN FOLIAR", "Expediente sin foliar"),
            ("EXPEDIENTE FOLIADO INCORRECTAMENTE", "Expediente foliado incorrectamente"),
            ("EXPEDIENTE DESGLOSADO", "Expediente desglosado"),
            ("EXPEDIENTE CON CARATULA EN MAL ESTADO", "Expediente con caratula en mal estado"),
            ("EXPEDIENTE SIN CARATULA", "Expediente sin caratula"),
            ("EXPEDIENTE SIN ESPECIFICACION DE TOMOS ENVIADOS", "Expediente sin especificación de tomos enviados"),
            ("EXPEDIENTE CON CAPTURA ERRONEA DE FOJAS", "Expediente con captura errónea de fojas"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "arc_remesas_documentos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    arc_documento_id = Column(Integer, ForeignKey("arc_documentos.id"), index=True, nullable=False)
    arc_documento = relationship("ArcDocumento", back_populates="arc_remesas_documentos")
    arc_remesa_id = Column(Integer, ForeignKey("arc_remesas.id"), index=True, nullable=False)
    arc_remesa = relationship("ArcRemesa", back_populates="arc_remesas_documentos")

    # Columnas
    anomalia = Column(
        Enum(*ANOMALIAS, name="anomalias", native_enum=False),
        nullable=False,
    )
    fojas = Column(Integer, nullable=False)
    observaciones_solicitante = Column(String(256))
    observaciones_archivista = Column(String(256))
    tipo_juzgado = Column(
        Enum(*TIPOS, name="tipos", native_enum=False),
        nullable=False,
    )

    def __repr__(self):
        """Representación"""
        return f"<ArcRemesaDocumento {self.id}>"
