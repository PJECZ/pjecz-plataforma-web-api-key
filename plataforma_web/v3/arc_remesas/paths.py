"""
Archivo - Remesas v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_arc_remesas, get_arc_remesa
from .schemas import ArcRemesaOut, OneArcRemesaOut

arc_remesas = APIRouter(prefix="/v3/arc_remesas", tags=["archivo"])


@arc_remesas.get("", response_model=CustomPage[ArcRemesaOut])
async def listado_arc_remesas(
    current_user: CurrentUser,
    db: DatabaseSession,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    estado: str = None,
):
    """Listado de remesas"""
    if current_user.permissions.get("ARC REMESAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_arc_remesas(
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


@arc_remesas.get("/{arc_remesa_id}", response_model=OneArcRemesaOut)
async def detalle_arc_remesa(
    current_user: CurrentUser,
    db: DatabaseSession,
    arc_remesa_id: int,
):
    """Detalle de una remesa a partir de su id"""
    if current_user.permissions.get("ARC REMESAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        arc_remesa = get_arc_remesa(db, arc_remesa_id)
    except MyAnyError as error:
        return OneArcRemesaOut(success=False, message=str(error))
    return OneArcRemesaOut.from_orm(arc_remesa)
