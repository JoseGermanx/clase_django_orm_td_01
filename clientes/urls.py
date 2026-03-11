
from django.urls import path, include
from .views import listar_clientes, clientes_activos, detalle_cliente

urlpatterns = [
   path('listar/',listar_clientes, name="listar"), #listar
   path('activos/', clientes_activos, name="activos"), #activos
   path('<int:cliente_id>/', detalle_cliente, name='detalle') #detalle
]