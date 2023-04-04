"""
PJECZ Plataforma Web API Key
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings

from .v3.abogados.paths import abogados
from .v3.audiencias.paths import audiencias
from .v3.autoridades.paths import autoridades
from .v3.bitacoras.paths import bitacoras
from .v3.distritos.paths import distritos
from .v3.edictos.paths import edictos
from .v3.entradas_salidas.paths import entradas_salidas
from .v3.epocas.paths import epocas
from .v3.glosas.paths import glosas
from .v3.listas_de_acuerdos.paths import listas_de_acuerdos
from .v3.materias.paths import materias
from .v3.materias_tipos_juicios.paths import materias_tipos_juicios
from .v3.modulos.paths import modulos
from .v3.peritos.paths import peritos
from .v3.peritos_tipos.paths import peritos_tipos
from .v3.permisos.paths import permisos
from .v3.redams.paths import redams
from .v3.repsvm_agresores.paths import repsvm_agresores
from .v3.roles.paths import roles
from .v3.sentencias.paths import sentencias
from .v3.tesis_jurisprudencias.paths import tesis_jurisprudencias
from .v3.usuarios.paths import usuarios
from .v3.usuarios_roles.paths import usuarios_roles
from .v3.ubicaciones_expedientes.paths import ubicaciones_expedientes


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Plataforma Web API Key",
        description="Bienvenido a PJECZ Plataforma Web API Key. Esta API es para trabajar con los datos de Plataforma Web. Se requiere tener una api-key para usarse.",
    )

    # CORSMiddleware
    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rutas
    app.include_router(abogados)
    app.include_router(audiencias)
    app.include_router(autoridades)
    app.include_router(bitacoras)
    app.include_router(distritos)
    app.include_router(edictos)
    app.include_router(entradas_salidas)
    app.include_router(epocas)
    app.include_router(glosas)
    app.include_router(listas_de_acuerdos)
    app.include_router(materias)
    app.include_router(materias_tipos_juicios)
    app.include_router(modulos)
    app.include_router(peritos)
    app.include_router(peritos_tipos)
    app.include_router(permisos)
    app.include_router(redams)
    app.include_router(repsvm_agresores)
    app.include_router(roles)
    app.include_router(sentencias)
    app.include_router(tesis_jurisprudencias)
    app.include_router(usuarios)
    app.include_router(usuarios_roles)
    app.include_router(ubicaciones_expedientes)

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "Bienvenido a PJECZ Plataforma Web API Key. Esta API es para trabajar con los datos de Plataforma Web. Se requiere tener una api-key para usarse."}

    # Entregar
    return app
