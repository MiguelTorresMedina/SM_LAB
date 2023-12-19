# Usa la imagen oficial de Python
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Expone el puerto 80
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
