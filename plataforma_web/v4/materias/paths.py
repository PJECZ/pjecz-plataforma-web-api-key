"""
Materias v3, rutas (paths)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList
from plataforma_web.core.permisos.models import Permiso
from plataforma_web.v4.materias.crud import get_materia_with_clave, get_materias
from plataforma_web.v4.materias.schemas import ItemMateriaOut, OneMateriaOut
from plataforma_web.v4.usuarios.authentications import AuthenticatedUser, get_current_active_user

materias = APIRouter(prefix="/v4/materias", tags=["materias"])


@materias.get("", response_model=CustomList[ItemMateriaOut])
async def listado_materias(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    en_sentencias: bool = None,
):
    """Listado de materias"""
    if current_user.permissions.get("MATERIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_materias(database, en_sentencias)
    except MyAnyError as error:
        return CustomList(success=False, message=str(error))
    return paginate(resultados)


@materias.get("/{materia_clave}", response_model=OneMateriaOut)
async def detalle_materia(
    current_user: Annotated[AuthenticatedUser, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    materia_clave: str,
):
    """Detalle de una materia a partir de su clave"""
    if current_user.permissions.get("MATERIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        materia = get_materia_with_clave(database, materia_clave)
    except MyAnyError as error:
        return OneMateriaOut(success=False, message=str(error))
    return OneMateriaOut.model_validate(materia)
