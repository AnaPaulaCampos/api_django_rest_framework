
class PedidoServices():



    def validarEstado(estadoAtual, novoEstado):
            RECEIVED = ["Confirmado", "Despachado", "Entregue","Cancelado"]
            CONFIRMED = ["Despachado", "Cancelado"]
            DISPATCHED = ["Entregue","Cancelado"]
            DELIVERED = []
            CANCELED = []


            if estadoAtual != novoEstado:
                if estadoAtual == "Despachado":
                    if novoEstado in DISPATCHED:
                        return True
            return False