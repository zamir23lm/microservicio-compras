from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    idUsuario = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nombre
    