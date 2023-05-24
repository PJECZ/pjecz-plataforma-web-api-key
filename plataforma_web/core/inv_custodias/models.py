"""
Inventarios Custodias, modelos
"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin

from ..distritos.models import Distrito


class InvCustodia(Base, UniversalMixin):
    """InvCustodia"""

    # Nombre de la tabla
    __tablename__ = "inv_custodias"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), index=True, nullable=False)
    usuario = relationship("Usuario", back_populates="inv_custodias")

    # Columnas
    fecha = Column(Date, nullable=False, index=True)
    curp = Column(String(256), nullable=True)
    nombre_completo = Column(String(256))

    # Hijos
    inv_equipos = relationship("InvEquipo", back_populates="inv_custodia")

    @property
    def distrito_id(self):
        """Id del distrito"""
        return self.usuario.oficina.distrito_id

    @property
    def distrito_clave(self):
        """Clave del distrito"""
        return self.usuario.oficina.distrito.clave

    @property
    def domicilio_edificio(self):
        """Edificio del domicilio"""
        return self.usuario.oficina.domicilio.edificio

    @property
    def oficina_id(self):
        """Id de la oficina"""
        return self.usuario.oficina_id

    @property
    def oficina_clave(self):
        """Clave de la oficina"""
        return self.usuario.oficina.clave

    @property
    def usuario_email(self):
        """Email del usuario"""
        return self.usuario.email

    def __repr__(self):
        """Representación"""
        return f"<InvCustodia {self.id}>"
