from pyexpat import model
import site
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Tipo_enlace(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100, null=False)
    num_contacto = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.proveedor

class Sitios(models.Model):
    sitio = models.CharField(max_length=100, null=False)
    num_contacto = models.CharField(max_length=100, null=False)
    persona_contacto = models.CharField(max_length=250, null=False)
    bandwitch = models.CharField(max_length=100, null=False)
    ubicacion = models.CharField(max_length=250, null=False)
    num_cliente = models.CharField(max_length=250, null=False)
    proveedor_1 = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=False)
    tipo_enlace = models.ForeignKey(Tipo_enlace, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.sitio

class Reclamos(models.Model):
    coment = RichTextField(null=False)
    num = models.IntegerField(null=False)
    contact = models.CharField(max_length=150, null=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    sitio = models.ForeignKey(Sitios, on_delete=models.CASCADE, null=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null = False)

    def __str__(self):
        return "Reclamo numero "+self.num+" pertenee al sitio "+self.sitio
        

