# 🧪 Apothecaria - Sistema de Gestión de Productos

Sistema web completo de gestión de productos alquímicos desarrollado con Django y MySQL. Este proyecto implementa operaciones CRUD completas, relaciones de base de datos avanzadas, y una interfaz moderna con Bootswatch Lux.

## 📋 Descripción del Proyecto

Aplicación web para gestionar una lista de productos y sus categorías. Los productos tienen nombre, descripción, precio y están asociados a categorías. El sistema permite la gestión completa a través de operaciones CRUD: crear, leer, actualizar y eliminar productos.

## 🎯 Funcionalidades Implementadas

### ✅ Requisitos Cumplidos

- **Conexión a MySQL**: Base de datos MySQL configurada y conectada
- **Modelos de Datos**: Producto, Categoría, Etiqueta y DetalleProducto
- **Relaciones Implementadas**:
  - 🔗 **Muchos a Uno**: Producto → Categoría (ForeignKey)
  - 🔗 **Muchos a Muchos**: Producto ↔ Etiqueta (ManyToManyField)
  - 🔗 **Uno a Uno**: Producto ↔ DetalleProducto (OneToOneField)
- **Operaciones CRUD**: Completas para Productos, Categorías y Etiquetas
- **Consultas ORM**: Filtros, búsquedas, exclude() y anotaciones
- **Migraciones**: Gestionadas correctamente
- **Seguridad**: Protección CSRF, autenticación de usuarios, login requerido
- **Django Admin**: Panel administrativo personalizado
- **Autenticación**: Sistema completo de login/logout

## 🏗️ Arquitectura del Sistema

### Modelos de Base de Datos

```python
# Categoría (Entidad independiente)
- nombre: CharField(max_length=100)
- descripcion: TextField()

# Producto (Entidad principal)
- nombre: CharField(max_length=100)
- descripcion: TextField()
- precio: DecimalField(max_digits=10, decimal_places=2)
- categoria: ForeignKey(Categoria) → Relación Muchos a Uno
- etiquetas: ManyToManyField(Etiqueta) → Relación Muchos a Muchos

# Etiqueta
- nombre: CharField(max_length=50)

# DetalleProducto (Relación Uno a Uno)
- producto: OneToOneField(Producto)
- detalles: TextField()
- dimensiones: CharField(max_length=100)
- peso: DecimalField(max_digits=10, decimal_places=2)
- imagen: ImageField(upload_to='productos/')
```

## 📁 Estructura del Proyecto

```
alquimia_premium/
│
├── productos/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── inicio.html
│   │   ├── login.html
│   │   ├── perfil_usuario.html
│   │   ├── crear_producto.html
│   │   ├── detalle_producto.html
│   │   ├── editar_producto.html
│   │   ├── eliminar_producto.html
│   │   ├── lista_productos.html
│   │   ├── crear_categoria.html
│   │   ├── editar_categoria.html
│   │   ├── eliminar_categoria.html
│   │   ├── lista_categorias.html
│   │   ├── crear_etiqueta.html
│   │   ├── editar_etiqueta.html
│   │   ├── eliminar_etiqueta.html
│   │   └── lista_etiquetas.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── media/
│   └── productos/
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Instalación y Configuración

### 1. Requisitos Previos

- Python 3.8 o superior
- MySQL 12 o superior
- pip (gestor de paquetes de Python)

### 2. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd alquimia_premium
```

### 3. Crear y Activar Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate
```

### 4. Instalar Dependencias

```bash
pip install django
pip install psycopg2-binary
pip install Pillow
```

O usar el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 5. Configurar MySQL

Crear la base de datos en MySQL:

```sql
-- Conectarse a MySQL
psql -U postgres

-- Crear base de datos
CREATE DATABASE alquimia_db;

-- Crear usuario
CREATE USER alquimia_user WITH PASSWORD 'tu_contraseña_segura';

-- Configurar encoding
ALTER ROLE alquimia_user SET client_encoding TO 'utf8';
ALTER ROLE alquimia_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE alquimia_user SET timezone TO 'America/Santiago';

-- Otorgar privilegios
GRANT ALL PRIVILEGES ON DATABASE alquimia_db TO alquimia_user;

-- Salir
\q
```

### 6. Configurar settings.py

Editar `settings.py` con la configuración de la base de datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.MySQL',
        'NAME': 'alquimia_db',
        'USER': 'alquimia_user',
        'PASSWORD': 'tu_contraseña_segura',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 7. Ejecutar Migraciones

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 8. Crear Superusuario

```bash
python manage.py createsuperuser
```

Ingresa:
- Username
- Email (opcional)
- Password

### 9. Ejecutar el Servidor

```bash
python manage.py runserver
```

Acceder a: `http://127.0.0.1:8000/`

## 🗺️ Rutas del Sistema

| Ruta | Nombre | Descripción |
|------|--------|-------------|
| `/` | inicio | Página de bienvenida |
| `/login` | login_usuario | Iniciar sesión |
| `/logout` | logout_usuario | Cerrar sesión |
| `/perfil` | perfil_usuario | Perfil de usuario |
| `/productos/lista` | lista_productos | Lista de productos |
| `/productos/crear` | crear_producto | Crear producto |
| `/productos/<int:pk>` | detalle_producto | Detalle de producto |
| `/productos/<int:pk>/editar` | editar_producto | Editar producto |
| `/productos/<int:pk>/eliminar` | eliminar_producto | Eliminar producto |
| `/categorias/lista` | lista_categorias | Lista de categorías |
| `/categorias/crear` | crear_categoria | Crear categoría |
| `/categorias/<int:pk>/editar` | editar_categoria | Editar categoría |
| `/categorias/<int:pk>/eliminar` | eliminar_categoria | Eliminar categoría |
| `/etiquetas/lista` | lista_etiquetas | Lista de etiquetas |
| `/etiquetas/crear` | crear_etiqueta | Crear etiqueta |
| `/etiquetas/<int:pk>/editar` | editar_etiqueta | Editar etiqueta |
| `/etiquetas/<int:pk>/eliminar` | eliminar_etiqueta | Eliminar etiqueta |
| `/admin/` | admin | Panel de administración |

## 💻 Ejemplos de Consultas ORM

### Consultas Básicas

```python
# Obtener todos los productos
productos = Producto.objects.all()

# Filtrar por nombre
producto = Producto.objects.filter(nombre__icontains='poción')

# Filtrar por categoría
productos_categoria = Producto.objects.filter(categoria__nombre='Pociones de Curación')

# Productos con precio mayor a 100
productos_caros = Producto.objects.filter(precio__gt=100)

# Excluir productos de una categoría
productos = Producto.objects.exclude(categoria__nombre='Ingredientes')
```

### Consultas Avanzadas

```python
# Productos con sus detalles (join)
from django.db.models import Q

productos_completos = Producto.objects.select_related('categoria', 'detalleproducto').all()

# Búsqueda múltiple con OR
productos = Producto.objects.filter(
    Q(nombre__icontains='fuego') | Q(descripcion__icontains='fuego')
)

# Contar productos por categoría
from django.db.models import Count

categorias = Categoria.objects.annotate(num_productos=Count('producto'))

# Precio promedio
from django.db.models import Avg

precio_promedio = Producto.objects.aggregate(Avg('precio'))

# Productos con etiquetas específicas
productos_raros = Producto.objects.filter(etiquetas__nombre='Raro')
```

### Consultas SQL Personalizadas

```python
# Usando raw()
productos = Producto.objects.raw('''
    SELECT p.* 
    FROM productos_producto p
    INNER JOIN productos_categoria c ON p.categoria_id = c.id
    WHERE c.nombre = %s AND p.precio > %s
''', ['Pociones', 50])

# Consulta compleja con detalles
productos_detallados = Producto.objects.raw('''
    SELECT p.id, p.nombre, p.precio, c.nombre as categoria_nombre, 
           d.peso, d.dimensiones
    FROM productos_producto p
    LEFT JOIN productos_categoria c ON p.categoria_id = c.id
    LEFT JOIN productos_detalleproducto d ON p.id = d.producto_id
    ORDER BY p.precio DESC
''')
```

## 🔒 Seguridad Implementada

### Protección CSRF

Todos los formularios incluyen el token CSRF:
```django
<form method="post">
    {% csrf_token %}
    <!-- campos del formulario -->
</form>
```

### Autenticación

Vistas protegidas con el decorador `@login_required`:
```python
from django.contrib.auth.decorators import login_required

@login_required
def crear_producto(request):
    # Solo usuarios autenticados pueden crear productos
    pass
```

### Middleware de Seguridad

Configurado en `settings.py`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## 🎨 Diseño y Frontend

- **Framework CSS**: Bootswatch Lux Theme
- **Iconos**: Font Awesome 6.4.2
- **Características**:
  - Diseño responsive
  - Gradientes modernos
  - Animaciones suaves
  - Cards con efectos hover
  - Sistema de mensajes con Bootstrap alerts

## 🔧 Panel de Administración

Acceder a: `http://127.0.0.1:8000/admin/`

### Funcionalidades del Admin

- Gestión completa de Productos, Categorías y Etiquetas
- Filtros por categoría y etiquetas
- Búsqueda por nombre y descripción
- Edición en línea de DetalleProducto
- Contador de productos por categoría
- Interfaz personalizada con títulos descriptivos

## 📸 Capturas de Pantalla

### Página de Inicio
![Página de Inicio](screenshots/inicio.png)
*Página principal con hero section y features*

### Lista de Productos
![Lista de Productos](screenshots/lista_productos.png)
*Grid de productos con cards responsive*

### Detalle de Producto
![Detalle de Producto](screenshots/detalle_producto.png)
*Vista detallada con imagen, descripción y detalles técnicos*

### Formulario de Creación
![Crear Producto](screenshots/crear_producto.png)
*Formulario completo con validación*

### Panel de Administración
![Django Admin](screenshots/admin.png)
*Panel administrativo personalizado*

## 🧪 Datos de Prueba

### Crear Categorías de Ejemplo

```python
python manage.py shell

from productos.models import Categoria

Categoria.objects.create(
    nombre="Pociones de Curación",
    descripcion="Elixires restauradores y bálsamos mágicos"
)

Categoria.objects.create(
    nombre="Pociones de Fuego",
    descripcion="Brebajes incendiarios y explosivos"
)

Categoria.objects.create(
    nombre="Ingredientes Raros",
    descripcion="Componentes exóticos para fórmulas avanzadas"
)
```

### Crear Etiquetas

```python
from productos.models import Etiqueta

Etiqueta.objects.create(nombre="Raro")
Etiqueta.objects.create(nombre="Popular")
Etiqueta.objects.create(nombre="Potente")
Etiqueta.objects.create(nombre="Natural")
```

## 🐛 Solución de Problemas Comunes

### Error de Conexión a MySQL

```bash
# Verificar que MySQL esté corriendo
sudo service MySQL status

# Verificar credenciales en settings.py
# Asegurarse que el usuario y contraseña coincidan
```

### Error con Pillow

```bash
# Instalar dependencias de sistema para Pillow
# En Ubuntu/Debian:
sudo apt-get install python3-dev python3-pip python3-venv
sudo apt-get install libjpeg-dev zlib1g-dev

# Reinstalar Pillow
pip uninstall Pillow
pip install Pillow
```

### Imágenes no se muestran

Verificar configuración en `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Y en `urls.py` principal:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 📦 Dependencias del Proyecto

```txt
Django==5.0
psycopg2-binary==2.9.9
Pillow==10.1.0
```

## 🤝 Contribuciones

Este proyecto es parte de una actividad evaluada. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de uso educativo.

## 👨‍💻 Autor

Desarrollado como parte del Módulo 7 - Evaluación del Módulo

