from datetime import date
from enum import Enum
from models.cliente import Cliente
from models.item_pedido import ItemPedido


class StatusPedido(Enum):
    PENDENTE = "PENDENTE"
    EM_PRODUCAO = "EM_PRODUCAO"
    FINALIZADO = "FINALIZADO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"

class Pedido:
    def __init__(self, id: int, cliente: Cliente):
        self.__id: int = id
        self.__data: date = date.today()
        self.__status: StatusPedido = StatusPedido.PENDENTE
        self.__cliente: Cliente = cliente
        self.__itens: list[ItemPedido] = []

    def get_id(self) -> int:
        return self.__id
    def get_data(self) -> date:
        return self.__data
    def get_status(self) -> StatusPedido:
        return self.__status
    def get_cliente(self) -> Cliente:
        return self.__cliente

    def get_itens(self) -> list[ItemPedido]:
        return self.__itens
    def calcular_total(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.calcular_subtotal()
        return total
    def alterar_status(self, novo_status: StatusPedido) -> None:
        self.__status = novo_status