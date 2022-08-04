from rest_framework import serializers

from api.models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Pedido
    fields = [
      'ID',
      'nomeCliente',
      'nomeProduto',
      'valorProduto',
      'estadoAtualPedido' ,
      'horarioCriacaoPedido' ,
    ]

class AtualizarPedidoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Pedido
    fields = [
      'ID',
      'estadoAtualPedido',
    ]
