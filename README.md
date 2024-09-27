# pjecz-plataforma-web-api-key

API con autentificación para consultar las bases de datos.

## Mejores practicas

Usa las recomendaciones de [I've been abusing HTTP Status Codes in my APIs for years](https://blog.slimjim.xyz/posts/stop-using-http-codes/)

### Respuesta exitosa

Status code: **200**

Respuesta como _paginado_ de items

```json
{
    "success": true,
    "message": "Success",
    "total": 2812,
    "items": [
        {
            "id": 123,
            ...
        },
        ...
    ],
    "limit": 100,
    "offset": 0
}
```

Respuesta de un _item_

```json
{
    "success": true,
    "message": "Success",
    "id": 123,
    ...
}
```

### Respuesta fallida: registro no encontrado

Status code: **200**

Body

```json
{
  "success": true,
  "message": "No existe ese abogado",
  "id": null,
  ...
}
```

### Respuesta fallida: ruta incorrecta

Status code: **404**

## Configure Poetry

Por defecto, con **poetry** el entorno se guarda en un directorio en `~/.cache/pypoetry/virtualenvs`

Modifique para que el entorno se guarde en el mismo directorio que el proyecto

```bash
poetry config --list
poetry config virtualenvs.in-project true
```

Verifique que este en True

```bash
poetry config virtualenvs.in-project
```

## Configuracion

**Para desarrollo** hay que crear un archivo para las variables de entorno `.env`

```ini
# Base de datos
DB_HOST=NNN.NNN.NNN.NNN
DB_PORT=5432
DB_NAME=pjecz_plataforma_web
DB_USER=adminpjeczplataformaweb
DB_PASS=XXXXXXXXXXXXXXXX

# CORS origins
ORIGINS=http://localhost:3000,http://localhost:5000,http://127.0.0.1:3000,http://127.0.0.1:5000

# Google Cloud Storage buckets
CLOUD_STORAGE_DEPOSITO=pjecz-desarrollo
CLOUD_STORAGE_DEPOSITO_EDICTOS=pjecz-desarrollo
CLOUD_STORAGE_DEPOSITO_GLOSAS=pjecz-desarrollo
CLOUD_STORAGE_DEPOSITO_LISTAS_DE_ACUERDOS=pjecz-desarrollo
CLOUD_STORAGE_DEPOSITO_SENTENCIAS=pjecz-desarrollo
CLOUD_STORAGE_DEPOSITO_USUARIOS=pjecz-desarrollo

# Salt sirve para cifrar el ID con HashID
SALT=XXXXXXXXXXXXXXXX
```

Cree un archivo `.bashrc` que se puede usar en el perfil de **Konsole**

```bash
if [ -f ~/.bashrc ]
then
    . ~/.bashrc
fi

if command -v figlet &> /dev/null
then
    figlet Plataforma Web API key
else
    echo "== Plataforma Web API key"
fi
echo

if [ -f .env ]
then
    echo "-- Variables de entorno"
    export $(grep -v '^#' .env | xargs)
    # source .env && export $(sed '/^#/d' .env | cut -d= -f1)
    echo "   DB_HOST: ${DB_HOST}"
    echo "   DB_PORT: ${DB_PORT}"
    echo "   DB_NAME: ${DB_NAME}"
    echo "   DB_USER: ${DB_USER}"
    echo "   DB_PASS: ${DB_PASS}"
    echo "   ORIGINS: ${ORIGINS}"
    echo "   SALT: ${SALT}"
    echo
    export PGHOST=$DB_HOST
    export PGPORT=$DB_PORT
    export PGDATABASE=$DB_NAME
    export PGUSER=$DB_USER
    export PGPASSWORD=$DB_PASS
fi

if [ -d .venv ]
then
    echo "-- Python Virtual Environment"
    source .venv/bin/activate
    echo "   $(python3 --version)"
    export PYTHONPATH=$(pwd)
    echo "   PYTHONPATH: ${PYTHONPATH}"
    echo
    echo "-- Poetry"
    export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
    echo "   $(poetry --version)"
    echo
    echo "-- FastAPI 127.0.0.1:8000"
    alias arrancar="uvicorn --factory --host=127.0.0.1 --port 8000 --reload plataforma_web.app:create_app"
    echo "   arrancar"
    echo
fi

if [ -d tests ]
then
    echo "-- Pruebas unitarias"
    echo "   python3 -m unittest discover tests"
    echo
fi

if [ -f .github/workflows/gcloud-app-deploy.yml ]
then
    echo "-- Google Cloud"
    echo "   GitHub Actions hace el deploy en Google Cloud"
    echo "   Si hace cambios en pyproject.toml reconstruya requirements.txt"
    echo "   poetry export -f requirements.txt --output requirements.txt --without-hashes"
    echo
fi
```

## Instalacion

En Fedora Linux agregue este software

```bash
sudo dnf -y groupinstall "Development Tools"
sudo dnf -y install glibc-langpack-en glibc-langpack-es
sudo dnf -y install pipenv poetry python3-virtualenv
sudo dnf -y install python3-devel python3-docs python3-idle
sudo dnf -y install python3.11
```

Clone el repositorio

```bash
cd ~/Documents/GitHub/PJECZ
git clone https://github.com/PJECZ/pjecz-plataforma-web-api-key.git
cd pjecz-plataforma-web-api-key
```

Instale el entorno virtual con **Python 3.11** y los paquetes necesarios

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install poetry
poetry install
```

## Arrancar para desarrollo

Ejecute `arrancar` que es un alias dentro de `.bashrc`

```bash
arrancar
```

## Pruebas

Para ejecutar las pruebas arranque el servidor y ejecute

```bash
python3 -m unittest discover tests
```

## Contenedores

Construir la imagen con el comando **podman**

```bash
podman build -t pjecz_plataforma_web_api_key .
```

Escribir el archivo `.env` con las variables de entorno

```ini
DB_HOST=NNN.NNN.NNN.NNN
DB_PORT=5432
DB_NAME=XXXXXXXXXXXXXXXX
DB_USER=XXXXXXXXXXXXXXXX
DB_PASS=XXXXXXXXXXXXXXXX
ORIGINS=*
SALT=XXXXXXXXXXXXXXXX
```

Arrancar el contenedor donde el puerto 8000 del contenedor se dirige al puerto **8002** local

```bash
podman run --rm \
    --name pjecz_plataforma_web_api_key \
    -p 8002:8000 \
    --env-file .env \
    pjecz_plataforma_web_api_key
```

Presionar CTRL-C para terminar la prueba anterior.

Arrancar el contenedor y dejar corriendo en el fondo

```bash
podman run -d \
    --name pjecz_plataforma_web_api_key \
    -p 8002:8000 \
    --env-file .env \
    pjecz_plataforma_web_api_key
```

Detener contenedor

```bash
podman container stop pjecz_plataforma_web_api_key
```

Arrancar contenedor

```bash
podman container start pjecz_plataforma_web_api_key
```

Eliminar contenedor

```bash
podman container rm pjecz_plataforma_web_api_key
```

Eliminar la imagen

```bash
podman image rm pjecz_plataforma_web_api_key
```

## Google Cloud deployment

Este proyecto usa **GitHub Actions** para subir a **Google Cloud**

Para ello debe crear el archivo `requirements.txt`

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
