class Usuario:
    def __init__(self, id: int, login: str, senha_hash: str):
        self.__id = id
        self.__login = login
        self.__senha_hash = senha_hash
    def get_id(self) -> int:
        return self.__id
    def get_login(self) -> str:
        return self.__login
    def get_senha_hash(self) -> str:
        return self.__senha_hash
    def autenticar(self, senha_hash: str) -> bool:
        return self.__senha_hash == senha_hash