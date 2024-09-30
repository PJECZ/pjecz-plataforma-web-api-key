"""
PJECZ Plataforma Web API key
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from fastapi_pagination import add_pagination

from config.settings import get_settings
from plataforma_web.v4.abogados.paths import abogados
from plataforma_web.v4.audiencias.paths import audiencias
from plataforma_web.v4.autoridades.paths import autoridades
from plataforma_web.v4.distritos.paths import distritos
from plataforma_web.v4.domicilios.paths import domicilios
from plataforma_web.v4.edictos.paths import edictos
from plataforma_web.v4.epocas.paths import epocas
from plataforma_web.v4.glosas.paths import glosas
from plataforma_web.v4.listas_de_acuerdos.paths import listas_de_acuerdos
from plataforma_web.v4.materias.paths import materias
from plataforma_web.v4.materias_tipos_juicios.paths import materias_tipos_juicios
from plataforma_web.v4.modulos.paths import modulos
from plataforma_web.v4.oficinas.paths import oficinas
from plataforma_web.v4.peritos.paths import peritos
from plataforma_web.v4.peritos_tipos.paths import peritos_tipos
from plataforma_web.v4.permisos.paths import permisos
from plataforma_web.v4.redam.paths import redam
from plataforma_web.v4.repsvm_agresores.paths import repsvm_agresores
from plataforma_web.v4.roles.paths import roles
from plataforma_web.v4.sentencias.paths import sentencias
from plataforma_web.v4.tesis_jurisprudencias.paths import tesis_jurisprudencias
from plataforma_web.v4.ubicaciones_expedientes.paths import ubicaciones_expedientes
from plataforma_web.v4.usuarios.paths import usuarios
from plataforma_web.v4.usuarios_roles.paths import usuarios_roles
from plataforma_web.v4.web_paginas.paths import web_paginas
from plataforma_web.v4.web_ramas.paths import web_ramas


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Plataforma Web API Key",
        description="API con autentificación para consultar las bases de datos.",
        docs_url="/docs",
        redoc_url=None,
    )

    # CORSMiddleware
    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["*"],
    )

    # Rutas
    app.include_router(abogados)
    app.include_router(audiencias)
    app.include_router(autoridades)
    app.include_router(distritos)
    app.include_router(domicilios)
    app.include_router(edictos)
    app.include_router(epocas)
    app.include_router(glosas)
    app.include_router(listas_de_acuerdos)
    app.include_router(materias)
    app.include_router(materias_tipos_juicios)
    app.include_router(modulos)
    app.include_router(oficinas)
    app.include_router(peritos)
    app.include_router(peritos_tipos)
    app.include_router(permisos)
    app.include_router(redam)
    app.include_router(repsvm_agresores)
    app.include_router(roles)
    app.include_router(sentencias)
    app.include_router(tesis_jurisprudencias)
    app.include_router(usuarios)
    app.include_router(usuarios_roles)
    app.include_router(ubicaciones_expedientes)
    app.include_router(web_paginas)
    app.include_router(web_ramas)

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "API con autentificación para consultar las bases de datos."}

    @app.get("/robots.txt", response_class=PlainTextResponse)
    async def robots():
        """robots.txt to disallow all agents"""
        return """User-agent: *\nDisallow: /"""

    # Entregar
    return app
