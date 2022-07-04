from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100)
    num_contacto = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.proveedor