from django.db import models
from django_enum import EnumField

# Create your models here.

class Cliente(models.Model):
    
    class TextEnum(models.TextChoices):
        VALUE0 = 'V0', 'VIP'
        VALUE1 = 'V1', 'regular'

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    tipo = EnumField(TextEnum, null=True)


    def __str__(self):
        return self.nombre