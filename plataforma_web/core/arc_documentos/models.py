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

    TIPO_JUZGADOS = OrderedDict(
        [
            ("ORAL", "Oral"),
            ("TRADICIONAL", "Tradicional"),
        ]
    )

    UBICACIONES = OrderedDict(
        [
            ("NO DEFINIDO", "No Definido"),
            ("ARCHIVO", "Archivo"),
            ("JUZGADO", "Juzgado"),
            ("REMESA", "Remesa"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "arc_documentos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    arc_juzgado_origen_id = Column(Integer, ForeignKey("arc_juzgados_extintos.id"), index=True, nullable=True)  # Puede ser NULL
    arc_juzgado_origen = relationship("ArcJuzgadoExtinto", back_populates="arc_documentos")
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="arc_documentos")

    # Columnas
    actor = Column(String(256), nullable=False)
    anio = Column(Integer, nullable=False)
    demandado = Column(String(256))
    expediente = Column(String(16), index=True, nullable=False)
    juicio = Column(String(128))
    fojas = Column(Integer, nullable=False)
    tipo_juzgado = Column(
        Enum(*TIPO_JUZGADOS, name="tipo_juzgados", native_enum=False),
        index=True,
        nullable=False,
    )
    ubicacion = Column(
        Enum(*UBICACIONES, name="ubicaciones", native_enum=False),
        index=True,
        nullable=False,
    )

    # Hijos
    arc_solicitudes = relationship("ArcSolicitud", back_populates="arc_documento")
    arc_remesas_documentos = relationship("ArcRemesaDocumento", back_populates="arc_documento")

    @property
    def arc_juzgado_origen_clave(self):
        """Juzgado de Origen clave"""
        return self.arc_juzgado_origen.clave if self.arc_juzgado_origen else None

    @property
    def arc_juzgado_origen_descripcion(self):
        """Juzgado de Origen descripción"""
        return self.arc_juzgado_origen.descripcion if self.arc_juzgado_origen else None

    @property
    def arc_juzgado_origen_descripcion_corta(self):
        """Juzgado de Origen descripción corta"""
        return self.arc_juzgado_origen.descripcion_corta if self.arc_juzgado_origen else None

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

    def __repr__(self):
        """Representación"""
        return f"<ArcDocumento {self.id}>"
