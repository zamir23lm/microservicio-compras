from django.urls import path
from .application.controllers import DireccionEnvioGuardar, DireccionEnvioDetalles, DireccionEnvioDelete, DireccioEnvioByUser, DireccionEnvioEditar

urlpatterns = [
    path('postear/', DireccionEnvioGuardar.as_view(), name='direccion-envio-guardar'),
    path('detalles/<int:direccionId>/', DireccionEnvioDetalles.as_view(), name='direccion-envio-detalles'),
    path('eliminar/<int:direccionId>/', DireccionEnvioDelete.as_view(), name='direccion-envio-eliminar'),
    path('usuario/<int:idUsuario>/', DireccioEnvioByUser.as_view(), name='direccion-envio-usuario'),
    path('editar/<int:direccionId>/<int:usuarioId>/', DireccionEnvioEditar.as_view(), name='direccion-envio-editar'),
]