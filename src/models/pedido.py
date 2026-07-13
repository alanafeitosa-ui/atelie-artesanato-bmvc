from models.item_pedido import ItemPedido

class Pedido:
    def __init__(self, id: int, cliente_id: int, data_pedido: str, status: str, valor_total: float):
        self.__id = id
        self.__cliente_id = cliente_id
        self.__data_pedido = data_pedido
        self.__status = status
        self.__valor_total = valor_total
        self.__itens = []  # lista de ItemPedido

    def get_id(self): return self.__id
    def get_cliente_id(self): return self.__cliente_id
    def get_data_pedido(self): return self.__data_pedido
    def get_status(self): return self.__status
    def get_valor_total(self): return self.__valor_total
    def get_itens(self): return self.__itens

    def set_status(self, status): self.__status = status
    def set_itens(self, itens): self.__itens = itens

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            cliente_id=row["cliente_id"],
            data_pedido=row["data_pedido"],
            status=row["status"],
            valor_total=row["valor_total"]
        )