from django.shortcuts import render

# Create your views here.

from api.serializers import AlunoSerializer
from rest_framework import viewsets, permissions
from api.models import Aluno


class AlunoViewSet(viewsets.ModelViewSet):
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  permission_classes = [permissions.IsAuthenticated]