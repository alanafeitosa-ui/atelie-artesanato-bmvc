class MateriaPrima:
    def __init__(self, id: int, nome: str, quantidade_estoque: float, unidade_medida: str, estoque_minimo: float):
        self.__id = id
        self.__nome = nome
        self.__quantidade_estoque = quantidade_estoque
        self.__unidade_medida = unidade_medida
        self.__estoque_minimo = estoque_minimo
    def get_id(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_quantidade_estoque(self) -> float:
        return self.__quantidade_estoque
    def get_unidade_medida(self) -> str:
        return self.__unidade_medida
    def get_estoque_minimo(self) -> float:
        return self.__estoque_minimo
    def set_estoque_minimo(self, estoque_minimo: float) -> None:
        if estoque_minimo <= 0:
            raise ValueError ("Valor menor ou igual a zero, verifique e tente novamente")
        else:
            self.__estoque_minimo = estoque_minimo
    def adicionar_quantidade(self, quantia: float) -> float:
        if quantia <= 0:
            raise ValueError("A quantia a adicionar deve ser maior do que zero!")
        else:
            self.__quantidade_estoque = self.__quantidade_estoque + quantia
            return self.__quantidade_estoque
    def consumir (self, quantia: float) -> float:
        if quantia > self.__quantidade_estoque or quantia<=0:
            raise ValueError("A quantia a ser consumida inserida é maior do que o estoque!")
        else:
            self.__quantidade_estoque = self.__quantidade_estoque - quantia
            return self.__quantidade_estoque
    def verificar_estoque(self) -> bool:
        if self.__quantidade_estoque < self.__estoque_minimo :
            return False
        else: 
            return True
       