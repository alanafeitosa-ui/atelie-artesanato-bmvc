class ClienteBoundary:
    @staticmethod
    def validar_criacao(dados: dict) -> dict:
        erros = {}
        if not dados.get("nome"):
            erros["nome"] = "Nome obrigatório."
        return erros

    @staticmethod
    def validar_edicao(dados: dict) -> dict:
        return ClienteBoundary.validar_criacao(dados)