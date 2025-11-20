from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'productos/inicio.html')

def lista_productos(request):
    from .models import Producto
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})