class MateriaPrimaBoundary:

    @staticmethod
    def validar_criacao(form: dict) -> dict:
        erros = {}
        if not form.get("nome"):
            erros["nome"] = "Nome obrigatório."
        if not form.get("unidade_medida"):
            erros["unidade_medida"] = "Unidade de medida obrigatória."
        try:
            qtd = float(form.get("quantidade_estoque", 0))
            if qtd < 0:
                erros["quantidade_estoque"] = "Estoque não pode ser negativo."
        except ValueError:
            erros["quantidade_estoque"] = "Quantidade inválida."
        try:
            minimo = float(form.get("estoque_minimo", 0))
            if minimo < 0:
                erros["estoque_minimo"] = "Estoque mínimo não pode ser negativo."
        except ValueError:
            erros["estoque_minimo"] = "Estoque mínimo inválido."
        return erros

    @staticmethod
    def validar_edicao(form: dict) -> dict:
        # Mesma lógica
        return MateriaPrimaBoundary.validar_criacao(form)