"""lotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from productos import views as vistaProductos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vistaProductos.inicio,name='inicio'),
    path('inmueble/cargar/',vistaProductos.cargarProducto,name='inmuebleCargar'),
    path('inmueble/listar/',vistaProductos.listarProductos,name='inmuebleListar'),
    path('inmueble/editar/',vistaProductos.existeProducto,name='existeProducto'),
    path('inmueble/editar/<int:id>',vistaProductos.editarProducto,name='inmuebleEditar'),
    path('inmueble/borrar/<int:id>',vistaProductos.borrarProducto,name='inmuebleBorrar'),
    path('fotos/cargar',vistaProductos.cargarFotos,name='fotosCargar'),
    path('fotos/listar/',vistaProductos.listarProductosFotos,name='inmuebleFotosListar'),
    path('fotos/listar/<int:id>',vistaProductos.listarProductosXFotos,name='fotosListar'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)