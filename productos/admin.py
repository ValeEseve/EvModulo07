from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Etiqueta, DetalleProducto

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Etiqueta)
admin.site.register(DetalleProducto)