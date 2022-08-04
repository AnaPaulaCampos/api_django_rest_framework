
from http.client import responses
import json
from api.api.serializers import AtualizarPedidoSerializer
from api.models import Pedido
from rest_framework.response import Response
from rest_framework.views import APIView



class AtualizarPedidoAPIView(APIView):
    serializer_class = AtualizarPedidoSerializer
    # throttle_scope = "cars_app"

   

    def put(self, request, *args, **kwargs):

        idPedido = request.query_params.get('id')
        # idPedido = request.query_params["ID"]
        pedido = Pedido.objects.get(ID=1)

        data = request.data

        pedido.estadoAtualPedido = data["estadoAtualPedido"]


        pedido.save()

        serializer = AtualizarPedidoSerializer(pedido)
        return Response(serializer.data)



    