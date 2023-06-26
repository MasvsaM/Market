from django.contrib import admin
from django.urls import path, include
from .views import lista_clientes, lista_productos, detalle_cliente, detalle_producto, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_cliente', detalle_cliente, name="detalle_cliente"),
    path('detalle_producto', detalle_producto, name="detalle_producto"),
    path('login', login, name="login"),
]
