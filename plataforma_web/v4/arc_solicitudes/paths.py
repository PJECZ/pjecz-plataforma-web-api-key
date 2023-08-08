"""
Archivo - Solicitudes v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_arc_solicitud, get_arc_solicitudes
from .schemas import ArcSolicitudOut, OneArcSolicitudOut

arc_solicitudes = APIRouter(prefix="/v4/arc_solicitudes", tags=["archivo"])


@arc_solicitudes.get("/paginado", response_model=CustomPage[ArcSolicitudOut])
async def listado_arc_solicitudes(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    estado: str = None,
):
    """Listado de solicitudes"""
    if current_user.permissions.get("ARC SOLICITUDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_arc_solicitudes(
            database=database,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            estado=estado,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@arc_solicitudes.get("/{arc_solicitud_id}", response_model=OneArcSolicitudOut)
async def detalle_arc_solicitud(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    arc_solicitud_id: int,
):
    """Detalle de una solicitud a partir de su id"""
    if current_user.permissions.get("ARC SOLICITUDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        arc_solicitud = get_arc_solicitud(database, arc_solicitud_id)
    except MyAnyError as error:
        return OneArcSolicitudOut(success=False, message=str(error))
    return OneArcSolicitudOut.model_validate(arc_solicitud)
