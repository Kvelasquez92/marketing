from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=100, blank = False, null = False)
    precio = models.FloatField()
    existencias = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', blank=False, null=False)
    descripcion = models.TextField(max_length=200, blank= True, null=True)

    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    precio = models.FloatField()
    descuento = models.FloatField()
    imagen = models.ImageField(upload_to='promociones', blank=False, null=False)
    productos = models.ManyToManyField(Receta, blank=False)
    descripcion = models.TextField(max_length=200, blank = True, null=True)

    def __str__(self):
        return self.nombre

class Suscriptores(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(max_length=100,null=False, blank=False)
