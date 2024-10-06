from django.contrib import admin

# Register your models here.
from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio
from apiPedidos.Usuario.domain.models import Usuario
admin.site.register(DireccionEnvio)
admin.site.register(Usuario)