from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField('Etiqueta', related_name='productos', blank=True)

    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    detalles = models.TextField()    
    dimensiones = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    def __str__(self):
        return f"Detalles de {self.producto.nombre}"