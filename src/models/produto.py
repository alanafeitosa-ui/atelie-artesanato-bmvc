from abc import ABC

class Produto(ABC):
    def __init__(self, id: int, nome: str, preco: float, categoria: str):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.__ativo = True

    def calcular_preco_final(self) -> float:
        return self.__preco

    # Getters
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_categoria(self) -> str:
        return self.__categoria

    def get_preco(self) -> float:
        return self.__preco

    def get_ativo(self) -> bool:
        return self.__ativo

    # Setters
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_categoria(self, categoria: str):
        self.__categoria = categoria

    def set_preco(self, preco: float):
        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero.")
        self.__preco = preco

    def excluir(self) -> None:
        self.__ativo = False

    @classmethod
    def from_row(cls, row):
        tipo = row["tipo"]
        if tipo == "pronta_entrega":
            return ProdutoProntaEntrega(
                id=row["id"],
                nome=row["nome"],
                preco=row["preco"],
                categoria=row["categoria"],
                quantidade_estoque=row["quantidade_estoque"]
            )
        elif tipo == "encomenda":
            return ProdutoEncomenda(
                id=row["id"],
                nome=row["nome"],
                preco=row["preco"],
                categoria=row["categoria"],
                prazo_entrega=row["prazo_entrega"],
                taxa_extra=row["taxa_extra"]
            )
        else:
            raise ValueError(f"Tipo de produto desconhecido: {tipo}")


class ProdutoProntaEntrega(Produto):
    def __init__(self, id: int, nome: str, preco: float, categoria: str, quantidade_estoque: int):
        super().__init__(id, nome, preco, categoria)
        self.__quantidade_estoque = quantidade_estoque

    def get_quantidade_estoque(self) -> int:
        return self.__quantidade_estoque

    def set_quantidade_estoque(self, quantidade_estoque: int):
        if quantidade_estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self.__quantidade_estoque = quantidade_estoque

    def baixar_estoque(self, quantidade_retirar: int) -> int:
        if quantidade_retirar > self.__quantidade_estoque or quantidade_retirar <= 0:
            raise ValueError("Quantidade inválida para retirada.")
        self.__quantidade_estoque -= quantidade_retirar
        return self.__quantidade_estoque

    def repor_estoque(self, quantidade_reposicao: int) -> int:
        if quantidade_reposicao <= 0:
            raise ValueError("Reposição deve ser positiva.")
        self.__quantidade_estoque += quantidade_reposicao
        return self.__quantidade_estoque


class ProdutoEncomenda(Produto):
    def __init__(self, id: int, nome: str, preco: float, categoria: str, prazo_entrega: int, taxa_extra: float):
        super().__init__(id, nome, preco, categoria)
        self.__prazo_entrega = prazo_entrega
        self.__taxa_extra = taxa_extra

    def calcular_preco_final(self) -> float:
        return super().calcular_preco_final() + self.__taxa_extra

    def get_prazo_entrega(self) -> int:
        return self.__prazo_entrega

    def get_taxa_extra(self) -> float:
        return self.__taxa_extra

    def set_prazo_entrega(self, prazo: int):
        if prazo < 0:
            raise ValueError("Prazo inválido.")
        self.__prazo_entrega = prazo

    def set_taxa_extra(self, taxa: float):
        if taxa < 0:
            raise ValueError("Taxa extra não pode ser negativa.")
        self.__taxa_extra = taxa