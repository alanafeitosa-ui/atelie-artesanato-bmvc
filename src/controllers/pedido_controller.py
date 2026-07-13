from models.pedido import Pedido

class PedidoController:

    pedidos = []

    @staticmethod
    def criar(pedido: Pedido) -> None:
        PedidoController.pedidos.append(pedido)

    @staticmethod
    def listar() -> list[Pedido]:
        return PedidoController.pedidos

    @staticmethod
    def buscar_por_id(id: int) -> Pedido | None:
        for pedido in PedidoController.pedidos:
            if pedido.get_id() == id:
                return pedido
        return None

    @staticmethod
    def alterar_status(id: int, novo_status) -> bool:
        pedido = PedidoController.buscar_por_id(id)
        if pedido:
            pedido.alterar_status(novo_status)
            return True
        return False

    @staticmethod
    def excluir(id: int) -> bool:
        pedido = PedidoController.buscar_por_id(id)
        if pedido:
            PedidoController.pedidos.remove(pedido)
            return True
        return False