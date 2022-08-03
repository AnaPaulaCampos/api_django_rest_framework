
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api import pedidosviewsets as pedidosViewSets

route = routers.DefaultRouter()

route.register(r'pedidos', pedidosViewSets.PedidoViewSet, basename='Pedidos'),
route.register(r'professor', pedidosViewSets.PedidoViewSet, basename='Professor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(route.urls))
]
