"""
Funcionarios v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_funcionario, get_funcionarios
from .schemas import FuncionarioOut, OneFuncionarioOut

funcionarios = APIRouter(prefix="/v3/funcionarios", tags=["funcionarios"])


@funcionarios.get("", response_model=CustomPage[FuncionarioOut])
async def listado_funcionarios(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    centro_trabajo_id: int = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
    en_funciones: bool = None,
    en_sentencias: bool = None,
    en_soportes: bool = None,
    en_tesis_jurisprudencias: bool = None,
):
    """Listado de funcionarios"""
    if current_user.permissions.get("FUNCIONARIOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_funcionarios(
            db=db,
            centro_trabajo_id=centro_trabajo_id,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            domicilio_id=domicilio_id,
            en_funciones=en_funciones,
            en_sentencias=en_sentencias,
            en_soportes=en_soportes,
            en_tesis_jurisprudencias=en_tesis_jurisprudencias,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@funcionarios.get("/{funcionario_id}", response_model=OneFuncionarioOut)
async def detalle_funcionario(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    funcionario_id: int,
):
    """Detalle de una funcionario a partir de su id"""
    if current_user.permissions.get("FUNCIONARIOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        funcionario = get_funcionario(db, funcionario_id)
    except MyAnyError as error:
        return OneFuncionarioOut(success=False, message=str(error))
    return OneFuncionarioOut.from_orm(funcionario)
