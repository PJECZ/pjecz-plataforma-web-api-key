"""
Funcionarios v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class FuncionarioOut(BaseModel):
    """Esquema para entregar funcionarios"""

    id: int | None = None
    centro_trabajo_id: int | None = None
    centro_trabajo_clave: str | None = None
    centro_trabajo_nombre: str | None = None
    nombres: str | None = None
    apellido_paterno: str | None = None
    apellido_materno: str | None = None
    curp: str | None = None
    email: str | None = None
    puesto: str | None = None
    en_funciones: bool | None = None
    en_sentencias: bool | None = None
    en_soportes: bool | None = None
    en_tesis_jurisprudencias: bool | None = None
    telefono: str | None = None
    extension: str | None = None
    domicilio_oficial: str | None = None
    ingreso_fecha: date | None = None
    puesto_clave: str | None = None
    fotografia_url: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneFuncionarioOut(FuncionarioOut, OneBaseOut):
    """Esquema para entregar un funcionario"""
