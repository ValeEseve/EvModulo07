from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

# USUARIO
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido de vuelta, {user.username}!')
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

@login_required
def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente')
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
    from django.shortcuts import get_object_or_404
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})

@login_required
def crear_producto(request):
    from .forms import ProductoForm
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    from .models import Producto
    from .forms import ProductoForm
    from django.shortcuts import get_object_or_404
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    from .models import Producto
    from django.shortcuts import get_object_or_404
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
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
            messages.success(request, 'Categoría creada exitosamente')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

@login_required
def editar_categoria(request, pk):
    from .models import Categoria
    from .forms import CategoriaForm
    from django.shortcuts import get_object_or_404
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, pk):
    from .models import Categoria
    from django.shortcuts import get_object_or_404
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente')
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
            messages.success(request, 'Etiqueta creada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'crear_etiqueta.html', {'form': form})

@login_required
def editar_etiqueta(request, pk):
    from .models import Etiqueta
    from .forms import EtiquetaForm
    from django.shortcuts import get_object_or_404
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta actualizada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'editar_etiqueta.html', {'form': form})

@login_required
def eliminar_etiqueta(request, pk):
    from .models import Etiqueta
    from django.shortcuts import get_object_or_404
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada exitosamente')
        return redirect('lista_etiquetas')
    return render(request, 'eliminar_etiqueta.html', {'etiqueta': etiqueta})