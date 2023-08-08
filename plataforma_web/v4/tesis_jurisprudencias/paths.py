"""
Tesis Jurisprudencias v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_tesis_jurisprudencia, get_tesis_jurisprudencias
from .schemas import OneTesisJurisprudenciaOut, TesisJurisprudenciaOut

tesis_jurisprudencias = APIRouter(prefix="/v4/tesis_jurisprudencias", tags=["tesis jurisprudencias"])


@tesis_jurisprudencias.get("/paginado", response_model=CustomPage[TesisJurisprudenciaOut])
async def listado_tesis_jurisprudencias(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de tesis jurisprudencias"""
    if current_user.permissions.get("TESIS JURISPRUDENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_tesis_jurisprudencias(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            epoca_id=epoca_id,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@tesis_jurisprudencias.get("/{tesis_jurisprudencia_id}", response_model=OneTesisJurisprudenciaOut)
async def detalle_tesisjurisprudencia(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    tesis_jurisprudencia_id: int,
):
    """Detalle de una tesis jurisprudencia a partir de su id"""
    if current_user.permissions.get("TESIS JURISPRUDENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        tesisjurisprudencia = get_tesis_jurisprudencia(database, tesis_jurisprudencia_id)
    except MyAnyError as error:
        return OneTesisJurisprudenciaOut(success=False, message=str(error))
    return OneTesisJurisprudenciaOut.model_validate(tesisjurisprudencia)
