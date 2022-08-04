from http.client import responses
from django.shortcuts import render

# Create your views here.

from api.api.serializers import PedidoSerializer
from rest_framework import viewsets
from api.models import Pedido


class PedidoViewSet(viewsets.ModelViewSet):
  queryset = Pedido.objects.all()
  serializer_class = PedidoSerializer
  
   

   