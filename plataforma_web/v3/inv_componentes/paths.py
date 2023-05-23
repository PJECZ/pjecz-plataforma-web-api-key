"""
Inventarios Componentes v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_inv_componentes, get_inv_componente
from .schemas import InvComponenteOut, OneInvComponenteOut

inv_componentes = APIRouter(prefix="/v3/inv_componentes", tags=["categoria"])


@inv_componentes.get("", response_model=CustomPage[InvComponenteOut])
async def listado_inv_componentes(
    current_user: CurrentUser,
    db: DatabaseSession,
    generacion: str = None,
    inv_categoria_id: int = None,
    inv_equipo_id: int = None,
):
    """Listado de componentes"""
    if current_user.permissions.get("INV COMPONENTES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_componentes(
            db=db,
            generacion=generacion,
            inv_categoria_id=inv_categoria_id,
            inv_equipo_id=inv_equipo_id,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@inv_componentes.get("/{inv_componente_id}", response_model=OneInvComponenteOut)
async def detalle_inv_componente(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_componente_id: int,
):
    """Detalle de una componente a partir de su id"""
    if current_user.permissions.get("INV COMPONENTES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_componente = get_inv_componente(db=db, inv_componente_id=inv_componente_id)
    except MyAnyError as error:
        return OneInvComponenteOut(success=False, message=str(error))
    return OneInvComponenteOut.from_orm(inv_componente)
