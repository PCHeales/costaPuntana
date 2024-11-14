from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
import datetime

def inicio(request):
    return render(request,'inicio.html')

#productos
def cargarProducto(request):
    if request.method == "GET":
        return render(request,"productos/cargar.html")
    elif request.method == "POST":
        Productos.objects.create(nombre=request.POST["nombre"],
            descripcion=request.POST["descripcion"],
            ubicacion=request.POST["ubicacion"],
            linkMaps=request.POST["linkMaps"],
            precio=request.POST["precio"],
            estado=True
            )
        return redirect("inmuebleListar")
    
def listarProductos(request):
    lista= Productos.objects.all()
    return render(request, 'productos/listar.html',{
        'lista':lista
    })

def existeProducto(request):
    if request.method == "GET":
        print("entro en editar GET")
    else:
        print("entro en editar POST")
        is_ajax = request.headers.get(
                'X-Requested-With') == 'XMLHttpRequest'
        data = {}
        if is_ajax:
            filas = [] 
            fila = []
            fila.append("a")
            fila.append("b")
            fila.append("c")
            filas.append(fila)
            data ['direccion'] = "/inmueble/editar/"+request.POST["id"]
            print (data["direccion"])
        return JsonResponse(data)

def editarProducto(request,id):
    if request.method == 'GET':
        producto=get_object_or_404(Productos,pk=id)
        print(producto.nombre)
        return render(request,'productos/editar.html',{
            "producto":producto
        })
    elif request.method=="POST":
        estadoRecibido=request.POST["estado"]=="activo"
        Productos.objects.filter(pk=request.POST["id"]).update(nombre=request.POST["nombre"],descripcion=request.POST["descripcion"],linkMaps=request.POST["linkMaps"],precio=request.POST["precio"],fechaAgregado=datetime.datetime.now(),estado=estadoRecibido)
        return redirect('inmuebleListar')

def borrarProducto(request,id):
    producto=get_object_or_404(Productos,pk=id)
    producto.delete()
    return redirect('inmuebleListar')  
#fin productos

#fotos
def cargarFotos(request):
    if request.method == "GET":
        lotes=Productos.objects.all()
        return render(request,"fotos/cargar.html",{
            "lotes":lotes
        })
    elif request.method == "POST":
        print(request.POST["lote"])
        archivos = request.FILES.getlist('archivo')
        print(len(archivos))
        producto=get_object_or_404(Productos,pk=request.POST["lote"])
        for archivo in archivos:
            Fotos.objects.create(archivo=archivo,producto=producto,descripcion=request.POST['descripcion'])
        return redirect("inmuebleFotosListar")

def listarProductosFotos(request):
    lista= Productos.objects.all()
    return render(request, 'fotos/listar.html',{
        'lista':lista,
    })
def listarProductosXFotos(request,id):
    lista= Fotos.objects.filter(producto=Productos.objects.get(pk=id))
    return render(request, 'fotos/listarXFoto.html',{
        'lista':lista,
    })
#fin fotos