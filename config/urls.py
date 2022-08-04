
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api import pedidosviewsets as pedidosViewSets
from api.api import atualizarpedidosview as atualizar
# from cars.api import CarsAPIView as carsview




route = routers.DefaultRouter()

route.register(r'pedidos', pedidosViewSets.PedidoViewSet, basename='Pedidos'),
# route.register(r'cars', viewsset.Car, basename='Pedidos'),

urlpatterns1 = [
    path('cars/', atualizar.AtualizarPedidoAPIView.as_view()),
    path('cars/<str:ID>/', atualizar.AtualizarPedidoAPIView.as_view()),
]

urlpatterns1 += route.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns1)),
]
