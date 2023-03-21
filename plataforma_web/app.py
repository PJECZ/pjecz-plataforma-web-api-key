"""
PJECZ Plataforma Web API Key
"""
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from .v3.bitacoras.paths import bitacoras
from .v3.entradas_salidas.paths import entradas_salidas
from .v3.modulos.paths import modulos
from .v3.permisos.paths import permisos
from .v3.roles.paths import roles
from .v3.usuarios.paths import usuarios
from .v3.usuarios_roles.paths import usuarios_roles

# FastAPI
app = FastAPI(
    title="PJECZ Plataforma Web API Key",
    description="API con autentificación para realizar operaciones con la base de datos de Plataforma Web.",
)

# Rutas
app.include_router(bitacoras)
app.include_router(entradas_salidas)
app.include_router(modulos)
app.include_router(permisos)
app.include_router(roles)
app.include_router(usuarios)
app.include_router(usuarios_roles)

# Paginación
add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a PJECZ Plataforma Web API Key."}
