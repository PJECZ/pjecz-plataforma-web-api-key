"""
Inventarios Componentes v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_inv_componente, get_inv_componentes
from .schemas import InvComponenteOut, OneInvComponenteOut

inv_componentes = APIRouter(prefix="/v3/inv_componentes", tags=["inventarios"])


@inv_componentes.get("", response_model=CustomPage[InvComponenteOut])
async def listado_inv_componentes(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
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
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@inv_componentes.get("/{inv_componente_id}", response_model=OneInvComponenteOut)
async def detalle_inv_componente(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    inv_componente_id: int,
):
    """Detalle de una componente a partir de su id"""
    if current_user.permissions.get("INV COMPONENTES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        inv_componente = get_inv_componente(db, inv_componente_id)
    except MyAnyError as error:
        return OneInvComponenteOut(success=False, message=str(error))
    return OneInvComponenteOut.from_orm(inv_componente)
