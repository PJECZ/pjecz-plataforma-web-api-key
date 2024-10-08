"""
Tesis Jurisprudencias v4, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage
from plataforma_web.core.permisos.models import Permiso
from plataforma_web.v4.tesis_jurisprudencias.crud import get_tesis_jurisprudencia, get_tesis_jurisprudencias
from plataforma_web.v4.tesis_jurisprudencias.schemas import ItemTesisJurisprudenciaOut, OneTesisJurisprudenciaOut
from plataforma_web.v4.usuarios.authentications import AuthenticatedUser, get_current_active_user

tesis_jurisprudencias = APIRouter(prefix="/v4/tesis_jurisprudencias", tags=["tesis jurisprudencias"])


@tesis_jurisprudencias.get("/{tesis_jurisprudencia_id}", response_model=OneTesisJurisprudenciaOut)
async def detalle_tesisjurisprudencia(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
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


@tesis_jurisprudencias.get("", response_model=CustomPage[ItemTesisJurisprudenciaOut])
async def paginado_tesis_jurisprudencias(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Paginado de tesis jurisprudencias"""
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
