"""
Inventarios Categorias v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_inv_categoria, get_inv_categorias
from .schemas import InvCategoriaOut, OneInvCategoriaOut

inv_categorias = APIRouter(prefix="/v4/inv_categorias", tags=["inventarios"])


@inv_categorias.get("/paginado", response_model=CustomPage[InvCategoriaOut])
async def listado_inv_categorias(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Listado de categorias"""
    if current_user.permissions.get("INV CATEGORIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_inv_categorias(database)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@inv_categorias.get("/{inv_categoria_id}", response_model=OneInvCategoriaOut)
async def detalle_inv_categoria(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    inv_categoria_id: int,
):
    """Detalle de una categoria a partir de su id"""
    if current_user.permissions.get("INV CATEGORIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_categoria = get_inv_categoria(database, inv_categoria_id)
    except MyAnyError as error:
        return OneInvCategoriaOut(success=False, message=str(error))
    return OneInvCategoriaOut.from_orm(inv_categoria)
