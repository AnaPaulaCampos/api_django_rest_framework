
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api import pedidosviewsets as pedidosViewSets
from api.api import atualizarpedidosview as atualizar




route = routers.DefaultRouter()

route.register(r'pedidos', pedidosViewSets.PedidoViewSet, basename='Pedidos'),

urlpatterns1 = [
    path('atualizar/', atualizar.AtualizarPedidoAPIView.as_view()),
    path('atualizar/<int:ID>/', atualizar.AtualizarPedidoAPIView.as_view()),
]

urlpatterns1 += route.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns1)),
]
