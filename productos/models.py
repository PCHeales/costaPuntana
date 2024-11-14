from django.db import models

class Productos(models.Model):
    nombre = models.TextField(max_length=150)
    descripcion = models.TextField(max_length=500)
    ubicacion = models.TextField(max_length=200)
    linkMaps = models.TextField(max_length=200)
    precio = models.FloatField()
    fechaAgregado = models.DateField(auto_now_add=True, blank=True)
    estado = models.BooleanField()

class Fotos(models.Model):
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    archivo = models.ImageField(upload_to='fotos/')
    descripcion = models.TextField(max_length=300)

class Categorias(models.Model):
    nombre = models.TextField(max_length=150)
    descripcion = models.TextField(max_length=300)

class ProductoCategoria(models.Model):
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE)

