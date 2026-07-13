class Cliente:
    def __init__(self, id: int, nome: str, telefone: str, email: str):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
    
    def get_id(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_telefone(self) -> str:
        return self.__telefone
    def get_email(self) -> str:
        return self.__email
    
    def atualizar_dados(self, nome: str, telefone: str, email: str) -> None:
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email