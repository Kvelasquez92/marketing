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
    imagen = models.ImageField(upload_to='promociones', blank=False, null=False)
    productos = models.ManyToManyField(producto, through='DetallePromocion')

    def __str__(self):
        return self.nombre

class DetallePromocion(models.Model):
    promocion = models.ForeignKey(Promocion, blank = False, null = False)
    producto = models.ForeignKey(Producto, blank=False, null=False)
    descuento = models.FloatField()

class Correo(models.Model):
    correo = models.EmailField(max_length=100)
