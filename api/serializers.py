from rest_framework import serializers

from api.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Aluno
    fields = [
      'nome',
      'codigo'
    ]

  