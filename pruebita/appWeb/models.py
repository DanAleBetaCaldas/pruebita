from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre  = models.TextField(max_length=100)
    activo  = models.BooleanField()

    def _str_ (self):
        return self.nombre

