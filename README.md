# Taller Sistemas Operativos - Servidores 2025

Este repositorio contiene el desarrollo de los puntos 1, 2 y 3 del taller de servidores.

## 📌 Requisitos previos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado en Windows con integración a **WSL 2** habilitada.  
- [Ngrok](https://ngrok.com/download) instalado en el sistema operativo.  
- Cuenta en Ngrok (para obtener su propio **authtoken**).  

---

## 📌 Estructura del proyecto
```
.
├── app/               # Código de la API (FastAPI + SQLite)
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 📌 Cómo correr el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU-USUARIO/servidores.git
cd servidores
```

### 2. Levantar la API con Docker
Construir la imagen y levantar el contenedor:
```bash
docker compose up --build -d
```

Verificar que el contenedor está corriendo:
```bash
docker ps
```

La API estará disponible en:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 3. Exponer la API con Ngrok
1. Instalar Ngrok según la guía oficial:  
   👉 [https://ngrok.com/download](https://ngrok.com/download)

2. Configurar su propio authtoken:  
   ```bash
   ngrok config add-authtoken SU_TOKEN_AQUI
   ```

3. Ejecutar el túnel apuntando al puerto 8000:  
   ```bash
   ngrok http 8000
   ```

4. Abrir la URL pública que genera Ngrok, ejemplo:  
   ```
   Forwarding  https://xxxx-1234.ngrok-free.app -> http://localhost:8000
   ```
   👉 `https://xxxx-1234.ngrok-free.app/docs`

Con esa URL, la API será accesible desde cualquier lugar de internet.

---

## 📌 Notas finales
- El `authtoken` de Ngrok es personal, por lo tanto **cada usuario debe configurar el suyo**.  
- Si desea detener el servicio, use:
  ```bash
  docker compose down
  ```

---
✅ Con esto se completan los **puntos 1, 2 y 3** del taller.

## 📌 Punto 4 – Segundo servicio desplegado con Docker + Ngrok

Además de la API en FastAPI, se agregó un servicio adicional con **Nginx** para demostrar la ejecución de múltiples servicios en contenedores.

### 1. Levantar Nginx con Docker
El archivo `docker-compose.yml` incluye un servicio adicional:

  web:
    image: nginx:alpine
    container_name: nginx_service
    ports:
      - "8080:80"
    restart: always

Esto levanta un servidor Nginx en el puerto **8080** de la máquina local.

Para levantar todos los servicios (API + Nginx):

docker compose up -d

### 2. Verificar el servicio
Abrir en el navegador:
👉 http://localhost:8080

Debería aparecer la página de inicio de **Nginx**.

### 3. Exponer Nginx con Ngrok
Ejecutar:

ngrok http 8080

Esto generará una URL pública, por ejemplo:

Forwarding  https://xxxx-1234.ngrok-free.app -> http://localhost:8080

De esta forma, el servicio Nginx es accesible desde cualquier lugar de internet.

---

✅ Con esto se completa el **punto 4**: se desplegó un servicio adicional (Nginx), se levantó en Docker y se expuso públicamente con Ngrok.
