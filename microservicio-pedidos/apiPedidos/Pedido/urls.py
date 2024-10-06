from django.urls import path
from .application.controllers import PedidoGuardar, DetallesPedidoId, PedidoByUserId, PedidoByUserIdAndPedidoId, PedidoByUserIdAndPedidoId, PedidoByUserIdAndEstado, PedidoByUserIdAndFechaPedido, PedidosByEstado, PedidosByRangeFechaPedido, PedidoEditar, PedidoDelete

urlpatterns = [
    path('postear/', PedidoGuardar.as_view(), name='pedido-guardar'),
    path('detalles/<int:pedidoId>/', DetallesPedidoId.as_view(), name='pedido-detalles'),
    path('usuario/<int:userId>/', PedidoByUserId.as_view(), name='pedido-user'),
    path('usuario/<int:userId>/pedido/<int:pedidoId>/', PedidoByUserIdAndPedidoId.as_view(), name='pedido-user-detalles'),
    path('usuario/<int:userId>/estado', PedidoByUserIdAndEstado.as_view(), name='pedido-estado'),
    path('usuario/<int:userId>/fecha', PedidoByUserIdAndFechaPedido.as_view(), name='pedido-fecha-usuario'),
    path('estado', PedidosByEstado.as_view(), name='pedido-estado-all'),
    path('fecha', PedidosByRangeFechaPedido.as_view(), name='pedido-fecha-all'),
    path('editar/<int:pedidoId>/', PedidoEditar.as_view(), name='pedido-editar'),
    path('eliminar/<int:pedidoId>/', PedidoDelete.as_view(), name='pedido-eliminar')
]