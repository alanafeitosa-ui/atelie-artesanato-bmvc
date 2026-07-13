class PedidoBoundary:
    @staticmethod
    def validar_criacao(dados: dict) -> dict:
        erros = {}
        if not dados.get("cliente_id"):
            erros["cliente_id"] = "Selecione um cliente."
        if not dados.get("itens"):
            erros["itens"] = "Adicione pelo menos um item."
        else:
            for i, item in enumerate(dados["itens"]):
                if not item.get("produto_id") or not item.get("quantidade") or not item.get("preco_unitario"):
                    erros["itens"] = f"Item {i+1} incompleto."
                    break
        return erros

    @staticmethod
    def validar_edicao(dados: dict) -> dict:
        # mesma validação básica
        return PedidoBoundary.validar_criacao(dados)