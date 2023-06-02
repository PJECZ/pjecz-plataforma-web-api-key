"""
Materias-Tipos de Juicios v3, rutas (paths)
"""
from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage, custom_page_success_false

from ...core.permisos.models import Permiso
from ..usuarios.authentications import CurrentUser

from .crud import get_materias_tipos_juicios, get_materia_tipo_juicio
from .schemas import MateriaTipoJuicioOut, OneMateriaTipoJuicioOut

materias_tipos_juicios = APIRouter(prefix="/v3/materias_tipos_juicios", tags=["materias"])


@materias_tipos_juicios.get("", response_model=CustomPage[MateriaTipoJuicioOut])
async def listado_materias_tipos_juicios(
    current_user: CurrentUser,
    db: DatabaseSession,
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de materias-tipos de juicios"""
    if current_user.permissions.get("MATERIAS TIPOS JUICIOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_materias_tipos_juicios(
            db=db,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return custom_page_success_false(error)
    return paginate(resultados)


@materias_tipos_juicios.get("/{materia_tipo_juicio_id}", response_model=OneMateriaTipoJuicioOut)
async def detalle_materia_tipo_juicio(
    current_user: CurrentUser,
    db: DatabaseSession,
    materia_tipo_juicio_id: int,
):
    """Detalle de una materia-tipo de juicio a partir de su id"""
    if current_user.permissions.get("MATERIAS TIPOS JUICIOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        materia_tipo_juicio = get_materia_tipo_juicio(db=db, materia_tipo_juicio_id=materia_tipo_juicio_id)
    except MyAnyError as error:
        return OneMateriaTipoJuicioOut(success=False, message=str(error))
    return OneMateriaTipoJuicioOut.from_orm(materia_tipo_juicio)
