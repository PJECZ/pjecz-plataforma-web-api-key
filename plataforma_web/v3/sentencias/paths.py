"""
Sentencias v3, rutas (paths)
"""
from datetime import date

from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_sentencias, get_sentencia
from .schemas import SentenciaOut, OneSentenciaOut

sentencias = APIRouter(prefix="/v3/sentencias", tags=["sentencias"])


@sentencias.get("", response_model=CustomPage[SentenciaOut])
async def listado_sentencias(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
    materia_tipo_juicio_id: int = None,
):
    """Listado de sentencias"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_sentencias(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            anio=anio,
            fecha=fecha,
            materia_tipo_juicio_id=materia_tipo_juicio_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@sentencias.get("/{sentencia_id}", response_model=OneSentenciaOut)
async def detalle_sentencia(
    current_user: CurrentUser,
    db: DatabaseSession,
    sentencia_id: int,
):
    """Detalle de una sentencia a partir de su id"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        sentencia = get_sentencia(db=db, sentencia_id=sentencia_id)
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    return OneSentenciaOut.from_orm(sentencia)
