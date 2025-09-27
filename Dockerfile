FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema mínimas
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY app ./app

# Directorio para la base de datos
RUN mkdir -p /data
ENV DB_URL=sqlite:////data/items.db

EXPOSE 8050

# Seguridad básica: usuario no root
RUN useradd -m appuser && chown -R appuser:appuser /app /data
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8050"]
