"""
Tesis Jurisprudencias v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_tesis_jurisprudencias, get_tesis_jurisprudencia
from .schemas import TesisJurisprudenciaOut, OneTesisJurisprudenciaOut

tesis_jurisprudencias = APIRouter(prefix="/v3/tesis_jurisprudencias", tags=["tesis jurisprudencias"])


@tesis_jurisprudencias.get("", response_model=CustomPage[TesisJurisprudenciaOut])
async def listado_tesis_jurisprudencias(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    epoca_id: int = None,
    materia_id: int = None,
):
    """Listado de tesis jurisprudencias"""
    if current_user.permissions.get("TESIS JURISPRUDENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_tesis_jurisprudencias(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            epoca_id=epoca_id,
            materia_id=materia_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@tesis_jurisprudencias.get("/{tesis_jurisprudencia_id}", response_model=OneTesisJurisprudenciaOut)
async def detalle_tesisjurisprudencia(
    current_user: CurrentUser,
    db: DatabaseSession,
    tesis_jurisprudencia_id: int,
):
    """Detalle de una tesis jurisprudencia a partir de su id"""
    if current_user.permissions.get("TESIS JURISPRUDENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        tesisjurisprudencia = get_tesis_jurisprudencia(db=db, tesis_jurisprudencia_id=tesis_jurisprudencia_id)
    except MyAnyError as error:
        return OneTesisJurisprudenciaOut(success=False, message=str(error))
    return OneTesisJurisprudenciaOut.from_orm(tesisjurisprudencia)
