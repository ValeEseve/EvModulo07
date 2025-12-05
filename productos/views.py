from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def lista_productos(request):
    from .models import Producto
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})