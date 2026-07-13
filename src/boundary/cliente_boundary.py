from controllers.cliente_controller import ClienteController
from models.cliente import Cliente


class ClienteBoundary:

    @staticmethod
    def cadastrar(id: int, nome: str, telefone: str, email: str) -> None:
        if not nome or not telefone or not email:
            raise ValueError("Todos os campos são obrigatórios.")

        cliente = Cliente(id, nome, telefone, email)
        ClienteController.criar(cliente)

    @staticmethod
    def listar():
        return ClienteController.listar()

    @staticmethod
    def buscar(id: int):
        return ClienteController.buscar_por_id(id)

    @staticmethod
    def atualizar(id: int, nome: str, telefone: str, email: str):
        return ClienteController.atualizar(id, nome, telefone, email)

    @staticmethod
    def excluir(id: int):
        return ClienteController.excluir(id)