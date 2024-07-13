"""
Tesis Jurisprudencias, modelos
"""

from datetime import date, datetime

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class TesisJurisprudencia(Base, UniversalMixin):
    """TesisJurisprudencia"""

    TIPOS = {
        "POR CONTRADICCION": "Por contradicción",
        "REITERACION": "reiteración",
        "REVALIDACION": "revalidación",
        "DECLARACION": "declaración",
    }

    ESTADOS = {
        "ACTIVAR": "ACTIVAR",
        "INTERRUMPIR": "Interrumpir",
        "MODIFICAR": "Modificar",
    }

    CLASES = {
        "TESIS": "Tesis",
        "JURISPRUDENCIA": "Jurisprudencia",
    }

    # Nombre de la tabla
    __tablename__ = "tesis_jurisprudencias"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    autoridad_id: Mapped[int] = mapped_column(ForeignKey("autoridades.id"))
    autoridad: Mapped["Autoridad"] = relationship(back_populates="tesis_jurisprudencias")
    epoca_id: Mapped[int] = mapped_column(ForeignKey("epocas.id"))
    epoca: Mapped["Epoca"] = relationship(back_populates="tesis_jurisprudencias")
    materia_id: Mapped[int] = mapped_column(ForeignKey("materias.id"))
    materia: Mapped["Materia"] = relationship(back_populates="tesis_jurisprudencias")

    # Columnas
    titulo: Mapped[str] = mapped_column(String(256))
    subtitulo: Mapped[str] = mapped_column(String(256))
    tipo: Mapped[str] = mapped_column(Enum(*TIPOS, name="tipos", native_enum=False), index=True)
    estado: Mapped[str] = mapped_column(Enum(*ESTADOS, name="estados", native_enum=False), index=True)
    clave_control: Mapped[str] = mapped_column(String(24))
    clase: Mapped[str] = mapped_column(Enum(*CLASES, name="clases", native_enum=False), index=True)
    rubro: Mapped[str] = mapped_column(String(256))
    texto: Mapped[str] = mapped_column(String(256))
    precedentes: Mapped[str] = mapped_column(String(256))
    votacion: Mapped[str] = mapped_column(String(256))
    votos_particulares: Mapped[str] = mapped_column(String(256))
    aprobacion_fecha: Mapped[date]
    publicacion_tiempo: Mapped[datetime]
    aplicacion_tiempo: Mapped[datetime]

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
    def epoca_nombre(self):
        """Nombre de la época"""
        return self.epoca.nombre

    @property
    def materia_clave(self):
        """Clave de la materia"""
        return self.materia.clave

    @property
    def materia_nombre(self):
        """Nombre de la materia"""
        return self.materia.nombre

    def __repr__(self):
        """Representación"""
        return f"<TesisJurisprudencia {self.id}>"
