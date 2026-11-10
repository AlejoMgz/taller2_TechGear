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

```text
techgear_project/
├── techgear_api/
│   ├── src/
│   │   ├── models/
│   │   │   └── user_model.py
│   │   ├── database.py
│   │   └── main.py
│   ├── .env
│   └── README.md
│
├── techgear_web/
│   ├── motos/
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── static/
│   │   │   └── motos/
│   │   │       └── images/
│   │   │           ├── apachetrtr.png
│   │   │           ├── boxer150.jpg
│   │   │           └── ns200.jpg
│   │   ├── templates/
│   │   │   └── motos/
│   │   │       ├── base.html
│   │   │       ├── catalogo.html
│   │   │       ├── dashboard.html
│   │   │       ├── detalle.html
│   │   │       ├── login.html
│   │   │       └── registro.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── techgear_web_core/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── db.sqlite3
│   ├── manage.py
│   ├── requirements.txt
│   └── vercel.json
│
├── .gitignore
└── README.md
```

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
