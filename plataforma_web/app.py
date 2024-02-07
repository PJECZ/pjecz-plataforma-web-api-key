"""
PJECZ Plataforma Web API Key
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings

from .v4.abogados.paths import abogados
from .v4.arc_documentos.paths import arc_documentos
from .v4.arc_juzgados_extintos.paths import arc_juzgados_extintos
from .v4.arc_remesas.paths import arc_remesas
from .v4.arc_remesas_documentos.paths import arc_remesas_documentos
from .v4.arc_solicitudes.paths import arc_solicitudes
from .v4.audiencias.paths import audiencias
from .v4.autoridades.paths import autoridades
from .v4.bitacoras.paths import bitacoras
from .v4.boletines.paths import boletines
from .v4.centros_trabajos.paths import centros_trabajos
from .v4.cit_dias_inhabiles.paths import cit_dias_inhabiles
from .v4.distritos.paths import distritos
from .v4.domicilios.paths import domicilios
from .v4.edictos.paths import edictos
from .v4.entradas_salidas.paths import entradas_salidas
from .v4.epocas.paths import epocas
from .v4.funcionarios.paths import funcionarios
from .v4.glosas.paths import glosas
from .v4.inv_categorias.paths import inv_categorias
from .v4.inv_componentes.paths import inv_componentes
from .v4.inv_custodias.paths import inv_custodias
from .v4.inv_equipos.paths import inv_equipos
from .v4.inv_marcas.paths import inv_marcas
from .v4.inv_modelos.paths import inv_modelos
from .v4.inv_redes.paths import inv_redes
from .v4.listas_de_acuerdos.paths import listas_de_acuerdos
from .v4.materias.paths import materias
from .v4.materias_tipos_juicios.paths import materias_tipos_juicios
from .v4.modulos.paths import modulos
from .v4.oficinas.paths import oficinas
from .v4.peritos.paths import peritos
from .v4.peritos_tipos.paths import peritos_tipos
from .v4.permisos.paths import permisos
from .v4.redam.paths import redam
from .v4.repsvm_agresores.paths import repsvm_agresores
from .v4.roles.paths import roles
from .v4.sentencias.paths import sentencias
from .v4.siga_bitacoras.paths import siga_bitacoras
from .v4.siga_grabaciones.paths import siga_grabaciones
from .v4.siga_salas.paths import siga_salas
from .v4.tesis_jurisprudencias.paths import tesis_jurisprudencias
from .v4.ubicaciones_expedientes.paths import ubicaciones_expedientes
from .v4.usuarios.paths import usuarios
from .v4.usuarios_roles.paths import usuarios_roles


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Plataforma Web API Key",
        description="API con autentificación para realizar operaciones con la base de datos de Plataforma Web.",
        docs_url="/docs",
        redoc_url=None,
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
    app.include_router(arc_documentos)
    app.include_router(arc_juzgados_extintos)
    app.include_router(arc_remesas)
    app.include_router(arc_remesas_documentos)
    app.include_router(arc_solicitudes)
    app.include_router(audiencias)
    app.include_router(autoridades)
    app.include_router(bitacoras)
    app.include_router(boletines)
    app.include_router(centros_trabajos)
    app.include_router(cit_dias_inhabiles)
    app.include_router(distritos)
    app.include_router(domicilios)
    app.include_router(edictos)
    app.include_router(entradas_salidas)
    app.include_router(epocas)
    app.include_router(funcionarios)
    app.include_router(glosas)
    app.include_router(inv_categorias)
    app.include_router(inv_componentes)
    app.include_router(inv_custodias)
    app.include_router(inv_equipos)
    app.include_router(inv_marcas)
    app.include_router(inv_modelos)
    app.include_router(inv_redes)
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
    app.include_router(siga_bitacoras)
    app.include_router(siga_grabaciones)
    app.include_router(siga_salas)
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
        return {"message": "API con autentificación para realizar operaciones con la base de datos de Plataforma Web."}

    # Entregar
    return app
