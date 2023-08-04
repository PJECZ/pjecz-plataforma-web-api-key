"""
Inventarios Custodias v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_inv_custodia, get_inv_custodias
from .schemas import InvCustodiaOut, OneInvCustodiaOut

inv_custodias = APIRouter(prefix="/v4/inv_custodias", tags=["inventarios"])


@inv_custodias.get("", response_model=CustomPage[InvCustodiaOut])
async def listado_inv_custodias(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    distrito_id: int = None,
    distrito_clave: str = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
    oficina_id: int = None,
    oficina_clave: str = None,
    usuario_id: int = None,
    usuario_email: str = None,
):
    """Listado de custodias"""
    if current_user.permissions.get("INV CUSTODIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_custodias(
            database=database,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
            oficina_id=oficina_id,
            oficina_clave=oficina_clave,
            usuario_id=usuario_id,
            usuario_email=usuario_email,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@inv_custodias.get("/{inv_custodia_id}", response_model=OneInvCustodiaOut)
async def detalle_inv_custodia(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    inv_custodia_id: int,
):
    """Detalle de una custodia a partir de su id"""
    if current_user.permissions.get("INV CUSTODIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_custodia = get_inv_custodia(database, inv_custodia_id)
    except MyAnyError as error:
        return OneInvCustodiaOut(success=False, message=str(error))
    return OneInvCustodiaOut.from_orm(inv_custodia)
