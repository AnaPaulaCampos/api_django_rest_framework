
from http.client import responses
import json
from api.api.pedidoservices import PedidoServices
from api.api.serializers import AtualizarPedidoSerializer
from api.models import Pedido
from rest_framework.response import Response
from rest_framework.views import APIView



class AtualizarPedidoAPIView(APIView):
    serializer_class = AtualizarPedidoSerializer

    # throttle_scope = "cars_app"

   

    # def put(self, request, *args, **kwargs):

    #     # idPedido = request.query_params.get('id')
    #     # idPedido = request.query_params["ID"]

    #     data = request.data
    #     pedido = Pedido.objects.get(ID=1)

    #     novoEstado = data["estadoAtualPedido"]

    #     podeAtualizarEstado = PedidoServices.validarEstado(pedido.estadoAtualPedido, novoEstado)

    #     if podeAtualizarEstado:
    #         pedido.estadoAtualPedido = novoEstado
        
    #     pedido.save()
    #     serializer = AtualizarPedidoSerializer(pedido)
    #     return Response(serializer.data)

    def put(self, request, *args, **kwargs):


        data = request.data
        pedido = Pedido.objects.get(ID=1)
        novoEstado = data["estadoAtualPedido"]
        podeAtualizarEstado = PedidoServices.validarEstado(pedido.estadoAtualPedido, novoEstado)

        try:
            if podeAtualizarEstado:
                pedido.estadoAtualPedido = novoEstado
                pedido.save()
                serializer = AtualizarPedidoSerializer(pedido)
            return Response(serializer.data)
        except podeAtualizarEstado:
            serializer = AtualizarPedidoSerializer(pedido)
            return Response({"message": "Deal doesnt exist"})






    