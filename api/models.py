from operator import mod
from django.db import models

# Create your models here.

class Pedido(models.Model):

    # RECEIVED, CONFIRMED, DISPATCHED, DELIVERED e CANCELED

    RECEIVED = "Recebido"
    CONFIRMED = "Confirmado"
    DISPATCHED = "Despachado"
    DELIVERED= "Entregue"
    CANCELED = "Cancelado"

    STATUS_PEDIDO = [
        (RECEIVED, "Recebido"),
        (CONFIRMED, "Confirmado"),
        (DISPATCHED, "Despachado"),
        (DELIVERED, "Entregue"),
        (CANCELED, "Cancelado"),
    ]

    ID = models.AutoField(primary_key=True, editable=False)
    nomeCliente = models.CharField(max_length=80)
    nomeProduto = models.CharField(max_length=80)
    valorProduto = models.FloatField()
    estadoAtualPedido = models.CharField(max_length=15, choices=STATUS_PEDIDO,
        default=RECEIVED,)
    horarioCriacaoPedido = models.DateTimeField(auto_now_add=True)









    