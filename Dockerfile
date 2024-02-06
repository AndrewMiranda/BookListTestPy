# Utiliza una imagen de Python como base
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual del directorio al directorio de trabajo
COPY . .

# Expone el puerto 8080
EXPOSE 8080

# Define la variable de entorno para Flask
ENV FLASK_APP=app.py

# Ejecuta la aplicación cuando el contenedor se inicia
CMD ["flask", "run", "--host=0.0.0.0"]
