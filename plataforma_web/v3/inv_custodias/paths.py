"""
Inventarios Custodias v3, rutas (paths)
"""
from datetime import date

from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_inv_custodias, get_inv_custodia
from .schemas import InvCustodiaOut, OneInvCustodiaOut

inv_custodias = APIRouter(prefix="/v3/inv_custodias", tags=["inventarios"])


@inv_custodias.get("", response_model=CustomPage[InvCustodiaOut])
async def listado_inv_custodias(
    current_user: CurrentUser,
    db: DatabaseSession,
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
            db=db,
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
        return custom_page_success_false(error)
    return paginate(resultados)


@inv_custodias.get("/{inv_custodia_id}", response_model=OneInvCustodiaOut)
async def detalle_inv_custodia(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_custodia_id: int,
):
    """Detalle de una custodia a partir de su id"""
    if current_user.permissions.get("INV CUSTODIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_custodia = get_inv_custodia(db, inv_custodia_id)
    except MyAnyError as error:
        return OneInvCustodiaOut(success=False, message=str(error))
    return OneInvCustodiaOut.from_orm(inv_custodia)
