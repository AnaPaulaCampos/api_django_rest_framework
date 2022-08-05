
class PedidoServices():

    RECEIVED = ["Confirmado", "Despachado", "Entregue","Cancelado"]
    CONFIRMED = ["Despachado", "Entregue","Cancelado"]
    DISPATCHED = ["Entregue","Cancelado"]
    DELIVERED = []
    CANCELED = []

    def validarEstado(estadoAtual, novoEstado):
            if estadoAtual != novoEstado:
                if estadoAtual == "Recebido":
                    if novoEstado in RECEIVED:
                        return True
                if estadoAtual == "Confirmado":
                    if novoEstado in CONFIRMED:
                        return True
                if estadoAtual == "Despachado":
                    if novoEstado in DISPATCHED:
                        return True
                if estadoAtual == "Entregue" or estadoAtual == "Cancelado":
                    return False
            return False