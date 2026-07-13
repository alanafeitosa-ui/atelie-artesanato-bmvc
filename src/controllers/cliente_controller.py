from models.cliente import Cliente

class ClienteController:

    clientes = []

    @staticmethod
    def criar(cliente: Cliente) -> None:
        ClienteController.clientes.append(cliente)

    @staticmethod
    def listar() -> list[Cliente]:
        return ClienteController.clientes

    @staticmethod
    def buscar_por_id(id: int) -> Cliente | None:
        for cliente in ClienteController.clientes:
            if cliente.get_id() == id:
                return cliente
        return None

    @staticmethod
    def atualizar(id: int, nome: str, telefone: str, email: str) -> bool:
        cliente = ClienteController.buscar_por_id(id)
        if cliente:
            cliente.atualizar_dados(nome, telefone, email)
            return True
        return False

    @staticmethod
    def excluir(id: int) -> bool:
        cliente = ClienteController.buscar_por_id(id)
        if cliente:
            ClienteController.clientes.remove(cliente)
            return True
        return False