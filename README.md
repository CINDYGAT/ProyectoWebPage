# ProyectoWebPage
Pagina web para el negocio Walter's Pizza

Activar entorno virtual (si es necesario)
source mi_entorno/bin/activate


En la terminal, dentro de la carpeta del proyecto

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver

runserver: para mostrar la pagina web en 127.0.0.0.1

makemigrations: cargar los modelos de models.py

migrate: para subir y hacer efectivos los modelos de models.py


-------------------------------------------------------------------------

Para correr el entorno virtual de Docker

cambiar en settings.py:

'HOST': 'db' # de "localhost" a "db"

En la terminal, dentro de la carpeta del proyecto:

docker-compose down 

docker-compose build

docker-compose up

