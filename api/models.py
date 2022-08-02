from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(
    max_length=20,
    null=False,
    blank=False)

    codigo = models.CharField(
    max_length=8,
    null=False,
    blank=False)

    