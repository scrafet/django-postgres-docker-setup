# Proyecto 03: Django + PostgreSQL + Docker 🚀

Este proyecto es una plantilla robusta y moderna para el desarrollo rápido de aplicaciones web utilizando **Django 5**, **PostgreSQL 15** y **Docker**. Incluye un panel de administración mejorado con **Jazzmin**, un dashboard frontend personalizado con **Bootstrap 5 (Dark Mode)**, y una configuración lista para desplegar.

## 🛠️ Tech Stack

*   **Backend**: Python 3.11, Django 5.0.1
*   **Base de Datos**: PostgreSQL 15
*   **Contenedores**: Docker & Docker Compose
*   **Frontend**: Bootstrap 5 (Bootswatch Darkly Theme), FontAwesome 6
*   **Admin Interface**: Django Jazzmin (Tema oscuro)
*   **Gestión de Entorno**: python-dotenv

## 📋 Prerrequisitos

Asegúrate de tener instalados:
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac/Linux)
*   Git

## 🚀 Despliegue Rápido (Quick Start)

Sigue estos pasos para levantar el proyecto en tu entorno local:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/scrafet/django-postgres-docker-setup.git
cd django-postgres-docker-setup
```

### 2. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto (junto al `docker-compose.yml`) con el siguiente contenido base:

```env
# Configuración de Django
DEBUG=True
SECRET_KEY=tu_clave_secreta_super_segura_aqui
ALLOWED_HOSTS=*

# Configuración de Base de Datos (PostgreSQL)
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### 3. Construir y Levantar Contenedores

```bash
docker-compose up -d --build
```

Esto descargará las imágenes necesarias, instalará las dependencias y levantará los servicios:
*   **web**: Accesible en `http://localhost:8000`
*   **db**: Base de datos PostgreSQL puerto 5432

### 4. Inicialización (Primera vez)

Una vez que los contenedores estén corriendo, aplica las migraciones y crea un superusuario.

**Aplicar Migraciones:**
```bash
docker-compose exec web python manage.py migrate
```

**Crear Superusuario (Admin):**
```bash
docker-compose exec web python manage.py createsuperuser
```
*(Sigue las instrucciones en pantalla para definir usuario y contraseña)*

## 🖥️ Acceso al Sistema

*   **Dashboard Principal**: [http://localhost:8000](http://localhost:8000)
    *   Requiere autenticación. Redirige automáticamente al Login.
*   **Panel de Administración (Jazzmin)**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

**Credenciales por defecto (si usaste el script de setup automático o promptMaestro):**
*   **Usuario**: `admin`
*   **Password**: `admin123`

## 📂 Estructura del Proyecto

```
proyecto-03-django/
├── app/                    # Código fuente de Django project
│   ├── core/               # App principal (Vistas, Modelos)
│   ├── myproject/          # Configuración (settings.py, urls.py)
│   ├── static/             # Archivos estáticos (CSS, JS, Imágenes)
│   └── templates/          # Plantillas HTML (Base, Includes, Vistas)
├── db_data/                # Persistencia de datos PostgreSQL (Ignorado por git)
├── .env                    # Variables de entorno (Ignorado por git)
├── Dockerfile              # Definición de imagen Python/Django
├── docker-compose.yml      # Orquestación de servicios
└── requirements.txt        # Dependencias de Python
```

## ✨ Características Clave

*   **Dashboard Moderno**: Layout responsivo con Sidebar, Header y Footer separados.
*   **Listado de Usuarios**: Vista de ejemplo en el dashboard que lista los usuarios reales del sistema con avatares generados.
*   **Seguridad**: `LoginRequiredMixin` implementado globalmente en las vistas protegidas.
*   **Consistencia Visual**: El frontend utiliza el tema "Darkly" para coincidir visualmente con el panel de administración de Jazzmin.

---
**Happy Coding!** 👨‍💻
