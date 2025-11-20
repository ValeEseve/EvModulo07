from django.urls import path
from .views import inicio, lista_productos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', lista_productos, name='lista_productos'),
]