from django.urls import path
from .application.controllers import UsuarioRegisterView, UsuarioLoginView, UsuarioDetalles, ObtenerId, UsuarioDetallesEmail, UsuarioDelete, UpdateUsuario, UsuarioUpdateEmail, updateTelefono

urlpatterns = [
    path('registrar/', UsuarioRegisterView.as_view(), name='usuario-registrar'),
    path('login/', UsuarioLoginView.as_view(), name='usuario-login'),
    path('detalles/<int:idUsuario>/', UsuarioDetalles.as_view(), name='usuario-detalles'),
    path('obtenerid/<int:idUsuario>/', ObtenerId.as_view(), name='usuario-obtenerid'),
    path('detalles-email/', UsuarioDetallesEmail.as_view(), name='usuario-detalles-email'),
    path('eliminar/<int:idUsuario>/', UsuarioDelete.as_view(), name='usuario-eliminar'),
    path('actualizar/<int:idUsuario>/', UpdateUsuario.as_view(), name='usuario-actualizar'),
    path('actualizar-email/<int:idUsuario>/', UsuarioUpdateEmail.as_view(), name='usuario-actualizar-email'),
    path('actualizar-telefono/<int:idUsuario>/', updateTelefono.as_view(), name='usuario-actualizar-password'),
]
