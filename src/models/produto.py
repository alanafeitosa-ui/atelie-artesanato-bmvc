from abc import ABC
class Produto(ABC):
    def __init__(self, id: int, nome: str, preco: float, categoria:str):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.__ativo = True
    def calcular_preco_final(self) -> float:
        return self.__preco
    def get_id(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_categoria(self) -> str:
        return self.__categoria
    def get_preco(self) -> float :
        return self.__preco
    def set_preco(self, preco: float) -> None:
        if preco <= 0:
            raise ValueError("Valor abaixo ou igual a zero, por favor revise!")
        else:
            self.__preco = preco
    def get_ativo(self) -> bool:
        return self.__ativo
    def excluir(self) -> None:
        self.__ativo = False
    
class ProdutoProntaEntrega(Produto):
    def __init__(self, id: int, nome: str, preco: float, categoria:str, quantidade_estoque: int):
        super().__init__(id, nome, preco, categoria)
        self.__quantidade_estoque = quantidade_estoque
    def get_quantidade_estoque(self) -> int:
        return self.__quantidade_estoque
    def set_quantidade_estoque(self, quantidade_estoque: int) -> None:
        if quantidade_estoque<0:
            raise ValueError("Atenção estoque negativo!")
        else:
            self.__quantidade_estoque = quantidade_estoque
    def baixar_estoque(self, quantidade_retirar: int) -> int:
        if quantidade_retirar > self.__quantidade_estoque or quantidade_retirar <= 0:
            raise ValueError("Quantia a ser retirada maior do que o estoque!")
        else: 
            self.__quantidade_estoque = self.__quantidade_estoque - quantidade_retirar
            return self.__quantidade_estoque
    def repor_estoque(self, quantidade_reposicao: int) -> int:
        if quantidade_reposicao<= 0 :
            raise ValueError("A quantia a ropor deve ser maior do que zero!")
        else:
            self.__quantidade_estoque = self.__quantidade_estoque + quantidade_reposicao
            return self.__quantidade_estoque

class ProdutoEncomenda(Produto):
    def __init__(self, id: int, nome: str, preco: float, categoria:str, prazo_entrega: int, taxa_extra: float):
        super().__init__(id, nome, preco, categoria)
        self.__prazo_entrega = prazo_entrega
        self.__taxa_extra = taxa_extra
    def calcular_preco_final(self) -> float:
        return (super().calcular_preco_final() + self.__taxa_extra)