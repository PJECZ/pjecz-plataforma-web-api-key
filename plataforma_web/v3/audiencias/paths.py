"""
Audiencias v3, rutas (paths)
"""
from datetime import date

from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_audiencias, get_audiencia
from .schemas import AudienciaOut, OneAudienciaOut

audiencias = APIRouter(prefix="/v3/audiencias", tags=["audiencias"])


@audiencias.get("", response_model=CustomPage[AudienciaOut])
async def listado_audiencias(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    anio: int = None,
    fecha: date = None,
):
    """Listado de audiencias"""
    if current_user.permissions.get("AUDIENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_audiencias(
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            anio=anio,
            fecha=fecha,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@audiencias.get("/{audiencia_id}", response_model=OneAudienciaOut)
async def detalle_audiencia(
    current_user: CurrentUser,
    db: DatabaseSession,
    audiencia_id: int,
):
    """Detalle de una audiencia a partir de su id"""
    if current_user.permissions.get("AUDIENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        audiencia = get_audiencia(db=db, audiencia_id=audiencia_id)
    except MyAnyError as error:
        return OneAudienciaOut(success=False, message=str(error))
    return OneAudienciaOut.from_orm(audiencia)
