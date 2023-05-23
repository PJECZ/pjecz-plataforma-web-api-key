"""
Oficinas v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_oficinas, get_oficina_with_clave
from .schemas import OficinaOut, OneOficinaOut

oficinas = APIRouter(prefix="/v3/oficinas", tags=["categoria"])


@oficinas.get("", response_model=CustomList[OficinaOut])
async def listado_oficinas(
    current_user: CurrentUser,
    db: DatabaseSession,
    distrito_id: int = None,
    distrito_clave: str = None,
    domicilio_id: int = None,
    es_jurisdiccional: bool = None,
):
    """Listado de oficinas"""
    if current_user.permissions.get("OFICINAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_oficinas(
            db=db,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            domicilio_id=domicilio_id,
            es_jurisdiccional=es_jurisdiccional,
        )
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@oficinas.get("/{clave}", response_model=OneOficinaOut)
async def detalle_oficina(
    current_user: CurrentUser,
    db: DatabaseSession,
    clave: str,
):
    """Detalle de una oficina a partir de su clave"""
    if current_user.permissions.get("OFICINAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        oficina = get_oficina_with_clave(db=db, clave=clave)
    except MyAnyError as error:
        return OneOficinaOut(success=False, message=str(error))
    return OneOficinaOut.from_orm(oficina)
