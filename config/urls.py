
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api import pedidosviewsets as pedidosViewSets
from cars.api.views import viewsets as viewsset
# from cars.api import CarsAPIView as carsview




route = routers.DefaultRouter()

route.register(r'pedidos', pedidosViewSets.PedidoViewSet, basename='Pedidos'),
# route.register(r'cars', viewsset.C PedidoViewSet, basename='Pedidos'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(route.urls)),
    path('', include('cars.api.urls')),
]
