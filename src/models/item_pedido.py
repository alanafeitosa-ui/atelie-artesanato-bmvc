class ItemPedido:
    def __init__(self, id: int, pedido_id: int, produto_id: int, quantidade: int, preco_unitario: float):
        self.__id = id
        self.__pedido_id = pedido_id
        self.__produto_id = produto_id
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario

    def get_id(self): return self.__id
    def get_pedido_id(self): return self.__pedido_id
    def get_produto_id(self): return self.__produto_id
    def get_quantidade(self): return self.__quantidade
    def get_preco_unitario(self): return self.__preco_unitario

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            pedido_id=row["pedido_id"],
            produto_id=row["produto_id"],
            quantidade=row["quantidade"],
            preco_unitario=row["preco_unitario"]
        )