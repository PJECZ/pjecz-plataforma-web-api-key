"""
Funcionarios v3, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class FuncionarioOut(BaseModel):
    """Esquema para entregar funcionarios"""

    id: int | None
    centro_trabajo_id: int | None
    centro_trabajo_clave: str | None
    centro_trabajo_nombre: str | None
    nombres: str | None
    apellido_paterno: str | None
    apellido_materno: str | None
    curp: str | None
    email: str | None
    puesto: str | None
    en_funciones: bool | None
    en_sentencias: bool | None
    en_soportes: bool | None
    en_tesis_jurisprudencias: bool | None
    telefono: str | None
    extension: str | None
    domicilio_oficial: str | None
    ingreso_fecha: date | None
    puesto_clave: str | None
    fotografia_url: str | None
    model_config = ConfigDict(from_attributes=True)


class OneFuncionarioOut(FuncionarioOut, OneBaseOut):
    """Esquema para entregar un funcionario"""
