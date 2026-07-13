from controllers.pedido_controller import PedidoController
from models.pedido import Pedido
from models.cliente import Cliente

class PedidoBoundary:

    @staticmethod
    def cadastrar(id: int, cliente: Cliente) -> None:
        pedido = Pedido(id, cliente)
        PedidoController.criar(pedido)

    @staticmethod
    def listar():
        return PedidoController.listar()

    @staticmethod
    def buscar(id: int):
        return PedidoController.buscar_por_id(id)

    @staticmethod
    def alterar_status(id: int, status):
        return PedidoController.alterar_status(id, status)

    @staticmethod
    def excluir(id: int):
        return PedidoController.excluir(id)