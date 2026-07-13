class Cliente:
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

    # Getters
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_telefone(self): return self.__telefone
    def get_email(self): return self.__email
    def get_endereco(self): return self.__endereco

    # Setters
    def set_nome(self, nome): self.__nome = nome
    def set_telefone(self, telefone): self.__telefone = telefone
    def set_email(self, email): self.__email = email
    def set_endereco(self, endereco): self.__endereco = endereco

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            nome=row["nome"],
            telefone=row["telefone"] or "",
            email=row["email"] or "",
            endereco=row["endereco"] or ""
        )