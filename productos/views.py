from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

# USUARIO
def login_usuario(request):
    return render(request, 'login.html')

@login_required
def logout_usuario(request):
    logout()
    return redirect('inicio')

@login_required
def perfil_usuario(request):
    return render(request, 'perfil_usuario.html', {'usuario': request.user})



# PRODUCTOS
def lista_productos(request):
    from .models import Producto
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    from .models import Producto
    producto = Producto.objects.get(pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})

@login_required
def crear_producto(request):
    from .forms import ProductoForm
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    from .models import Producto
    from .forms import ProductoForm
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    from .models import Producto
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})


# CATEGORIAS
def lista_categorias(request):
    from .models import Categoria
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    from .forms import CategoriaForm
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

@login_required
def editar_categoria(request, pk):
    from .models import Categoria
    from .forms import CategoriaForm
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, pk):
    from .models import Categoria
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'eliminar_categoria.html', {'categoria': categoria})

# ETIQUETAS
def lista_etiquetas(request):
    from .models import Etiqueta
    etiquetas = Etiqueta.objects.all()
    return render(request, 'lista_etiquetas.html', {'etiquetas': etiquetas})

@login_required
def crear_etiqueta(request):
    from .forms import EtiquetaForm
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'crear_etiqueta.html', {'form': form})

@login_required
def editar_etiqueta(request, pk):
    from .models import Etiqueta
    from .forms import EtiquetaForm
    etiqueta = Etiqueta.objects.get(pk=pk)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'editar_etiqueta.html', {'form': form})

@login_required
def eliminar_etiqueta(request, pk):
    from .models import Etiqueta
    etiqueta = Etiqueta.objects.get(pk=pk)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'eliminar_etiqueta.html', {'etiqueta': etiqueta})



