# Floralis Web 🌸

Aplicación web de e-commerce para una florería, desarrollada con **Django** por estudiantes de la **Tecnicatura Universitaria en Programación (TUP) - UTN FRLP**.

## Descripción

Floralis permite:

- Visualizar productos y categorías.
- Ver detalle de cada producto.
- Gestionar carrito de compras (agregar/eliminar productos).
- Realizar checkout para crear pedidos.
- Registrarse e iniciar/cerrar sesión.
- Enviar mensajes desde un formulario de contacto.
- Administrar datos desde el panel de Django Admin.

## Tecnologías

- Python 3
- Django 5
- SQLite3
- HTML + plantillas de Django

## Estructura del proyecto

- `floreria/`: configuración principal del proyecto Django.
- `tienda/`: lógica de catálogo, carrito y pedidos.
- `usuarios/`: registro y autenticación.
- `contacto/`: formulario de contacto.
- `templates/`: plantillas base del sitio.
- `media/`: archivos subidos (imágenes de productos).

## Requisitos

- Python 3.10+ (recomendado)
- pip
- (Opcional) entorno virtual

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd TUP-App-Florerias
```

2. Crear y activar entorno virtual (opcional, recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
```

3. Instalar Django:

```bash
pip install django
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Ejecutar servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abrir en navegador:

- Sitio principal: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Rutas principales

- `/` → Inicio tienda
- `/carrito/` → Carrito
- `/checkout/` → Finalizar compra
- `/contacto/` → Formulario de contacto
- `/usuarios/login/` → Login
- `/usuarios/registro/` → Registro

## Datos de desarrollo

Si necesitás administrar productos/categorías desde el panel de Django:

```bash
python manage.py createsuperuser
```

## Estado del proyecto

Proyecto académico en evolución para prácticas de desarrollo web con Django.

---

Hecho con 💐 por estudiantes de **TUP - UTN FRLP**.
