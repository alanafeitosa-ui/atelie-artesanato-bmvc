from models.produto import Produto
class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int, valor_unitario: float):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor_unitario = valor_unitario

    def get_produto(self) -> Produto:
        return self.__produto
    def get_quantidade(self) -> int:
        return self.__quantidade
    def get_valor_unitario(self) -> float:
        return self.__valor_unitario
    def calcular_subtotal(self) -> float:
        return self.__quantidade * self.__valor_unitario