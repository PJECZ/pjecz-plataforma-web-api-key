"""
Inventarios Equipos, modelos
"""
from collections import OrderedDict

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class InvEquipo(Base, UniversalMixin):
    """InvEquipo"""

    TIPOS = OrderedDict(
        [
            ("COMPUTADORA", "COMPUTADORA"),
            ("LAPTOP", "LAPTOP"),
            ("IMPRESORA", "IMPRESORA"),
            ("MULTIFUNCIONAL", "MULTIFUNCIONAL"),
            ("TELEFONIA", "TELEFONIA"),
            ("SERVIDOR", "SERVIDOR"),
            ("SCANNER", "SCANNER"),
            ("SWITCH", "SWITCH"),
            ("VIDEOGRABACION", "VIDEOGRABACION"),
            ("OTROS", "OTROS"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "inv_equipos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    inv_custodia_id = Column(Integer, ForeignKey("inv_custodias.id"), index=True, nullable=False)
    inv_custodia = relationship("InvCustodia", back_populates="inv_equipos")
    inv_modelo_id = Column(Integer, ForeignKey("inv_modelos.id"), index=True, nullable=False)
    inv_modelo = relationship("InvModelo", back_populates="inv_equipos")
    inv_red_id = Column(Integer, ForeignKey("inv_redes.id"), index=True, nullable=False)
    inv_red = relationship("InvRed", back_populates="inv_equipos")

    # Columnas
    fecha_fabricacion = Column(Date())
    numero_serie = Column(String(256))
    numero_inventario = Column(Integer())
    descripcion = Column(String(256), nullable=False)
    tipo = Column(Enum(*TIPOS, name="tipos", native_enum=False), index=True, nullable=False)
    direccion_ip = Column(String(256))
    direccion_mac = Column(String(256))
    numero_nodo = Column(Integer())
    numero_switch = Column(Integer())
    numero_puerto = Column(Integer())

    # Hijos
    inv_componentes = relationship("InvComponente", back_populates="inv_equipo")

    @property
    def inv_custodia_nombre_completo(self):
        """Nombre completo de la custodia"""
        return self.inv_custodia.nombre_completo

    @property
    def distrito_id(self):
        """Id del distrito"""
        return self.inv_custodia.usuario.oficina.distrito_id

    @property
    def distrito_clave(self):
        """Clave del distrito"""
        return self.inv_custodia.usuario.oficina.distrito.clave

    @property
    def domicilio_edificio(self):
        """Edificio del domicilio"""
        return self.inv_custodia.usuario.oficina.domicilio.edificio

    @property
    def inv_marca_id(self):
        """ID de la marca"""
        return self.inv_modelo.inv_marca_id

    @property
    def inv_marca_nombre(self):
        """Nombre de la marca"""
        return self.inv_modelo.inv_marca.nombre

    @property
    def inv_modelo_descripcion(self):
        """Descripción del modelo"""
        return self.inv_modelo.descripcion

    @property
    def inv_red_nombre(self):
        """Nombre de la red"""
        return self.inv_red.nombre

    @property
    def oficina_id(self):
        """ID de la oficina"""
        return self.inv_custodia.usuario.oficina_id

    @property
    def oficina_clave(self):
        """Clave de la oficina"""
        return self.inv_custodia.usuario.oficina.clave

    @property
    def usuario_id(self):
        """ID del usuario"""
        return self.inv_custodia.usuario_id

    @property
    def usuario_email(self):
        """Email del usuario"""
        return self.inv_custodia.usuario.email

    @property
    def disco_duro(self):
        """Disco duro"""
        for inv_componente in self.inv_componentes:
            if inv_componente.inv_categoria.nombre == "DISCO DURO":
                return f"{inv_componente.descripcion}; {inv_componente.version}"
        return ""

    @property
    def memoria_ram(self):
        """Memoria RAM"""
        for inv_componente in self.inv_componentes:
            if inv_componente.inv_categoria.nombre == "MEMORIA RAM":
                return inv_componente.descripcion
        return ""

    @property
    def procesador(self):
        """Procesador"""
        for inv_componente in self.inv_componentes:
            if inv_componente.inv_categoria.nombre == "PROCESADOR":
                return f"{inv_componente.descripcion}; {inv_componente.generacion}; {inv_componente.version}"
        return ""

    def __repr__(self):
        """Representación"""
        return f"<InvEquipo {self.id}>"
