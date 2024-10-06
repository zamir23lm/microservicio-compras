from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Configuración para Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de Pedidos",
      default_version='v1',
      description="Documentación de la API de Pedidos y sus servicios",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="soporte@pedidos.com"),
      license=openapi.License(name="Licencia BSD"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
@api_view(['GET'])
def welcome(request):
    return Response({'message': 'Bienvenido a la API de Pedidos'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),  # Endpoint de bienvenida

    
    path('api/usuario/', include('apiPedidos.Usuario.urls')),
    path('api/direccion/', include('apiPedidos.DireccionEnvio.urls')),
    path('api/pedido/', include('apiPedidos.Pedido.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
