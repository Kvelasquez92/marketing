from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank = False, null = False)
    precio = models.FloatField()
    existencias = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', blank=False, null=False)

    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    precio = models.FloatField()
    descuento = models.FloatField()
    imagen = models.ImageField(upload_to='promociones', blank=False, null=False)
    productos = models.ManyToManyField(Producto, blank=False)

    def __str__(self):
        return self.nombre

class Correo(models.Model):
    correo = models.EmailField(max_length=100)
