"""
Archivo - Solicitudes v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_arc_solicitudes, get_arc_solicitud
from .schemas import ArcSolicitudOut, OneArcSolicitudOut

arc_solicitudes = APIRouter(prefix="/v3/arc_solicitudes", tags=["archivo"])


@arc_solicitudes.get("", response_model=CustomPage[ArcSolicitudOut])
async def listado_arc_solicitudes(
    current_user: CurrentUser,
    db: DatabaseSession,
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
            db=db,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            estado=estado,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@arc_solicitudes.get("/{arc_solicitud_id}", response_model=OneArcSolicitudOut)
async def detalle_arc_solicitud(
    current_user: CurrentUser,
    db: DatabaseSession,
    arc_solicitud_id: int,
):
    """Detalle de una solicitud a partir de su id"""
    if current_user.permissions.get("ARC SOLICITUDES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        arc_solicitud = get_arc_solicitud(db, arc_solicitud_id)
    except MyAnyError as error:
        return OneArcSolicitudOut(success=False, message=str(error))
    return OneArcSolicitudOut.from_orm(arc_solicitud)
