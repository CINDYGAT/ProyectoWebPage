# Imagen base de Python
FROM python:3.10.12

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Configurar el directorio de trabajo
WORKDIR /proyecto

# Copiar los archivos de tu aplicación al contenedor
COPY . /proyecto/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Comando para ejecutar la aplicación
#CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

# Copiar el script entrypoint
COPY entrypoint.sh /proyecto/entrypoint.sh
# Configurar el entrypoint para el contenedor
ENTRYPOINT ["/proyecto/entrypoint.sh"]


