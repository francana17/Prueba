# Imagen base con Python
FROM python:3.11-slim

# Crear directorio de trabajo en el contenedor
WORKDIR /app

# Copiar todos los archivos del proyecto
COPY . /app

# Instalar las dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exponer el puerto que usa Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
