"""
Inventarios Categorias v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_inv_categorias, get_inv_categoria
from .schemas import InvCategoriaOut, OneInvCategoriaOut

inv_categorias = APIRouter(prefix="/v3/inv_categorias", tags=["inventarios"])


@inv_categorias.get("", response_model=CustomPage[InvCategoriaOut])
async def listado_inv_categorias(
    current_user: CurrentUser,
    db: DatabaseSession,
):
    """Listado de categorias"""
    if current_user.permissions.get("INV CATEGORIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_categorias(db)
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@inv_categorias.get("/{inv_categoria_id}", response_model=OneInvCategoriaOut)
async def detalle_inv_categoria(
    current_user: CurrentUser,
    db: DatabaseSession,
    inv_categoria_id: int,
):
    """Detalle de una categoria a partir de su id"""
    if current_user.permissions.get("INV CATEGORIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_categoria = get_inv_categoria(db, inv_categoria_id)
    except MyAnyError as error:
        return OneInvCategoriaOut(success=False, message=str(error))
    return OneInvCategoriaOut.from_orm(inv_categoria)
