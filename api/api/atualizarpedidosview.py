
from api.api.pedidoservices import PedidoServices
from api.api.serializers import AtualizarPedidoSerializer
from api.models import Pedido
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status




class AtualizarPedidoAPIView(APIView):
    serializer_class = AtualizarPedidoSerializer

    def put(self, request, *args, **kwargs):
        ID = request.POST.get('ID')
        pedido = Pedido.objects.get(ID=1)
        data = request.data
        podeAtualizarEstado = PedidoServices.validarEstado(pedido.estadoAtualPedido, data["estadoAtualPedido"])

        try:
            if podeAtualizarEstado:
                pedido.estadoAtualPedido = novoEstado
                pedido.save()
                serializer = AtualizarPedidoSerializer(pedido)
            return Response(serializer.data)
        except:  
            return Response({"message": "Mudanca de Estado NAO permitido !", "Pedido": {pedido.estadoAtualPedido}},status = status.HTTP_400_BAD_REQUEST )






    