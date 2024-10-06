from django.db import models
from apiPedidos.Usuario.domain.models import Usuario

class DireccionEnvio(models.Model):
    direccionId = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direccion_pedido')
    direccion = models.CharField(max_length=300)
    distrito = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigoPostal = models.CharField(max_length=10, blank=True, null=True)
    instrucciones = models.CharField(max_length=500, blank=True, null=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.direccion
