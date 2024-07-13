"""
Funcionarios, modelos
"""

from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Funcionario(Base, UniversalMixin):
    """Funcionario"""

    # Nombre de la tabla
    __tablename__ = "funcionarios"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Clave foránea
    centro_trabajo_id: Mapped[int] = mapped_column(ForeignKey("centros_trabajos.id"))
    centro_trabajo: Mapped["CentroTrabajo"] = relationship(back_populates="funcionarios")

    # Columnas
    nombres: Mapped[str] = mapped_column(String(256))
    apellido_paterno: Mapped[str] = mapped_column(String(256))
    apellido_materno: Mapped[str] = mapped_column(String(256))
    curp: Mapped[str] = mapped_column(String(18), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(256), unique=True, index=True)
    puesto: Mapped[str] = mapped_column(String(256))
    en_funciones: Mapped[bool] = mapped_column(default=True)
    en_sentencias: Mapped[bool] = mapped_column(default=True)
    en_soportes: Mapped[bool] = mapped_column(default=False)
    en_tesis_jurisprudencias: Mapped[bool] = mapped_column(default=False)
    telefono: Mapped[str] = mapped_column(String(48))
    extension: Mapped[str] = mapped_column(String(24))
    domicilio_oficial: Mapped[str] = mapped_column(String(512))
    ingreso_fecha: Mapped[date]
    puesto_clave: Mapped[str] = mapped_column(String(32))
    fotografia_url: Mapped[str] = mapped_column(String(512))

    @property
    def centro_trabajo_clave(self):
        """Clave del centro de trabajo"""
        return self.centro_trabajo.clave

    @property
    def centro_trabajo_nombre(self):
        """Nombre del centro de trabajo"""
        return self.centro_trabajo.nombre

    @property
    def nombre(self):
        """Junta nombres, apellido_paterno y apellido materno"""
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno

    def __repr__(self):
        """Representación"""
        return f"<Funcionario {self.id}>"
