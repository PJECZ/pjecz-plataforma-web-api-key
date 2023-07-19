"""
Sentencias v3, rutas (paths)
"""
from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ...core.sentencias.models import Sentencia
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import create_sentencia, delete_sentencia, get_sentencia, get_sentencias, update_sentencia
from .schemas import OneSentenciaOut, SentenciaIn, SentenciaOut

sentencias = APIRouter(prefix="/v3/sentencias", tags=["sentencias"])


@sentencias.get("", response_model=CustomPage[SentenciaOut])
async def listado_sentencias(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    anio: int = None,
    autoridad_id: int = None,
    autoridad_clave: str = None,
    distrito_id: int = None,
    distrito_clave: str = None,
    expediente: str = None,
    fecha: date = None,
    materia_tipo_juicio_id: int = None,
    sentencia: str = None,
):
    """Listado de sentencias"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_sentencias(
            db=db,
            anio=anio,
            autoridad_id=autoridad_id,
            autoridad_clave=autoridad_clave,
            distrito_id=distrito_id,
            distrito_clave=distrito_clave,
            expediente=expediente,
            fecha=fecha,
            materia_tipo_juicio_id=materia_tipo_juicio_id,
            sentencia=sentencia,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@sentencias.get("/{sentencia_id}", response_model=OneSentenciaOut)
async def detalle_sentencia(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    sentencia_id: int,
):
    """Detalle de una sentencia a partir de su id"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        sentencia = get_sentencia(db, sentencia_id)
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    return OneSentenciaOut.from_orm(sentencia)


@sentencias.post("", response_model=OneSentenciaOut)
async def crear_sentencia(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    sentencia_in: SentenciaIn,
):
    """Crear una sentencia"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.CREAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        sentencia = create_sentencia(db, Sentencia(**sentencia_in.dict()))
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    respuesta = OneSentenciaOut.from_orm(sentencia)
    respuesta.message = "Sentencia creada correctamente"
    return respuesta


@sentencias.put("/{sentencia_id}", response_model=OneSentenciaOut)
async def modificar_sentencia(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    sentencia_id: int,
    sentencia_in: SentenciaIn,
):
    """Modificar una sentencia"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.MODIFICAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        sentencia = update_sentencia(db, sentencia_id, Sentencia(**sentencia_in.dict()))
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    respuesta = OneSentenciaOut.from_orm(sentencia)
    respuesta.message = "Sentencia actualizada correctamente"
    return respuesta


@sentencias.delete("/{sentencia_id}", response_model=OneSentenciaOut)
async def borrar_sentencia(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
    sentencia_id: int,
):
    """Borrar una sentencia"""
    if current_user.permissions.get("SENTENCIAS", 0) < Permiso.BORRAR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        sentencia = delete_sentencia(db, sentencia_id)
    except MyAnyError as error:
        return OneSentenciaOut(success=False, message=str(error))
    respuesta = OneSentenciaOut.from_orm(sentencia)
    respuesta.message = "Sentencia eliminada correctamente"
    return respuesta
