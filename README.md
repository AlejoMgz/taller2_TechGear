Markdown
# 🏍️ TechGear Motos - Plataforma de Gestión y Catálogo

## 📌 Descripción
**TechGear Motos** es una aplicación web full-stack moderna desarrollada como una plataforma centralizada para la exploración, comercialización y administración de motocicletas de alto rendimiento. Cuenta con una interfaz intuitiva bajo un estilo *Clean Tech*, un diseño altamente accesible, responsive y optimizado para lograr un rendimiento y métricas óptimas en accesibilidad y velocidad. Incluye un sistema de roles diferenciados (Clientes y Administradores) con capacidades CRUD completas.

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Backend:** Python, Django (Arquitectura MVT).
* **Frontend:** HTML5, Bootstrap 5.3.2, JavaScript (ES6).
* **Gestión de Datos y Sesiones:** Sesiones firmadas de Django (`django.contrib.sessions.backends.signed_cookies`) optimizadas para entornos serverless.
* **Control de Versiones y Despliegue:** Git, GitHub, Vercel.

---

## 📁 Estructura del Proyecto

El repositorio se encuentra organizado de la siguiente manera:

techgear_project/
│
├── techgear_api/                  # Módulo de servicios de API backend
│   ├── src/
│   │   ├── models/                # Modelos de datos de la API
│   │   │   └── user_model.py
│   │   ├── database.py            # Configuración de base de datos para la API
│   │   └── main.py                # Archivo principal de ejecución de la API
│   ├── .env                       # Variables de entorno de la API
│   └── README.md
│
├── techgear_web/                  # Aplicación principal Django (Frontend y MVT)
│   ├── motos/
│   │   ├── migrations/            # Carpeta de migraciones de la base de datos
│   │   │   └── __init__.py
│   │   ├── static/                # Archivos estáticos
│   │   │   └── motos/
│   │   │       └── images/        # Recursos gráficos locales optimizados
│   │   │           ├── apachetrtr.png
│   │   │           ├── boxer150.jpg
│   │   │           └── ns200.jpg
│   │   ├── templates/             # Plantillas HTML de la interfaz
│   │   │   └── motos/
│   │   │       ├── base.html      # Plantilla principal con Navbar y Footer
│   │   │       ├── catalogo.html  # Vista del catálogo de motocicletas
│   │   │       ├── dashboard.html # Panel administrativo con CRUD modal
│   │   │       ├── detalle.html   # Vista detallada y ficha técnica
│   │   │       ├── login.html     # Formulario de inicio de sesión
│   │   │       └── registro.html  # Formulario de registro de usuarios
│   │   ├── __init__.py
│   │   ├── admin.py               # Configuración del panel de administración nativo
│   │   ├── apps.py                # Configuración de la aplicación motos
│   │   ├── models.py              # Modelos de datos de Django
│   │   ├── tests.py               # Pruebas unitarias
│   │   ├── urls.py                # Enrutador de la app de motos
│   │   └── views.py               # Lógica de negocio, autenticación y CRUD
│   │
│   ├── techgear_web_core/         # Configuración central de Django
│   │   ├── __init__.py
│   │   ├── asgi.py                # Configuración asíncrona
│   │   ├── settings.py            # Configuración general y de seguridad del proyecto
│   │   ├── urls.py                # URLs principales del proyecto web
│   │   └── wsgi.py                # Configuración para despliegue en servidor
│   │
│   ├── db.sqlite3                 # Base de datos local SQLite
│   ├── manage.py                  # Script de gestión y comandos de Django
│   ├── requirements.txt           # Dependencias y librerías del sistema web
│   └── vercel.json                # Archivo de configuración para el despliegue en Vercel
│
├── .gitignore                     # Archivos y carpetas ignoradas por Git
└── README.md                      # Documentación completa del repositorio

🛡️ Manejo de Excepciones
El sistema incorpora robustas estrategias de control de errores y excepciones para garantizar la continuidad operativa y una excelente experiencia de usuario:

Control de Conectividad con la API: Manejo de excepciones ante caídas de servicios externos o tiempos de espera agotados, asegurando que la interfaz muestre alertas amigables en lugar de interrumpir la ejecución.

Validación de Inventario (Productos sin stock): Restricciones lógicas en vistas y procesos de compra para evitar transacciones o asignaciones sobre modelos agotados.

Seguridad y Control de Acceso por Roles: Redireccionamientos automáticos y validaciones de sesión activas para impedir que usuarios comunes accedan a rutas o paneles administrativos (/dashboard).

⚙️ Instalación y Ejecución Local
Sigue estos pasos para levantar el entorno de desarrollo en tu máquina:

Clonar el repositorio:

Bash
git clone https://github.com/AlejoMgz/taller2_TechGear.git
cd techgear_project/techgear_web
Crear y activar el entorno virtual:

Bash
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate
Instalar las dependencias:

Bash
pip install -r requirements.txt
Aplicar migraciones y ejecutar el servidor local:

Bash
python manage.py migrate
python manage.py runserver
Accede a la aplicación en tu navegador a través de: http://127.0.0.1:8000/

🌐 Aplicación Despliegue
Vercel: taller2-tech-gear.vercel.app
Render: https://techgear-api-4o81.onrender.com

👨‍💻 Autor
Alejandro Mesa Gutiérrez
Ficha: 3494620