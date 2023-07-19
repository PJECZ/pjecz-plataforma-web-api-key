"""
Centros de Trabajo v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_centro_trabajo_with_clave, get_centros_trabajos
from .schemas import CentroTrabajoOut, OneCentroTrabajoOut

centros_trabajos = APIRouter(prefix="/v3/centros_trabajos", tags=["funcionarios"])


@centros_trabajos.get("", response_model=CustomPage[CentroTrabajoOut])
async def listado_centros_trabajos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
):
    """Listado de centros de trabajos"""
    if current_user.permissions.get("CENTROS TRABAJOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_centros_trabajos(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            domicilio_id=domicilio_id,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@centros_trabajos.get("/{centro_trabajo_clave}", response_model=OneCentroTrabajoOut)
async def detalle_centro_trabajo(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    centro_trabajo_clave: str,
):
    """Detalle de una centro de trabajo a partir de su clave"""
    if current_user.permissions.get("CENTROS TRABAJOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        centro_trabajo = get_centro_trabajo_with_clave(db, centro_trabajo_clave)
    except MyAnyError as error:
        return OneCentroTrabajoOut(success=False, message=str(error))
    return OneCentroTrabajoOut.from_orm(centro_trabajo)
