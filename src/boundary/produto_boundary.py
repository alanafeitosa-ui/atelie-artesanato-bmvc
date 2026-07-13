class ProdutoBoundary:

    @staticmethod
    def validar_criacao(form: dict) -> dict:
        erros = {}
        if not form.get("nome"):
            erros["nome"] = "Nome é obrigatório."
        try:
            preco = float(form["preco"])
            if preco <= 0:
                erros["preco"] = "Preço deve ser maior que zero."
        except (ValueError, KeyError):
            erros["preco"] = "Preço inválido."
        tipo = form.get("tipo")
        if tipo not in ("pronta_entrega", "encomenda"):
            erros["tipo"] = "Tipo inválido."
        # Validações específicas
        if tipo == "pronta_entrega":
            try:
                qtd = int(form.get("quantidade_estoque", 0))
                if qtd < 0:
                    erros["quantidade_estoque"] = "Estoque não pode ser negativo."
            except ValueError:
                erros["quantidade_estoque"] = "Quantidade inválida."
        elif tipo == "encomenda":
            try:
                prazo = int(form.get("prazo_entrega", 0))
                if prazo < 0:
                    erros["prazo_entrega"] = "Prazo não pode ser negativo."
            except ValueError:
                erros["prazo_entrega"] = "Prazo inválido."
            try:
                taxa = float(form.get("taxa_extra", 0.0))
                if taxa < 0:
                    erros["taxa_extra"] = "Taxa extra não pode ser negativa."
            except ValueError:
                erros["taxa_extra"] = "Taxa extra inválida."
        if not form.get("categoria"):
            erros["categoria"] = "Categoria é obrigatória."
        return erros

    @staticmethod
    def validar_edicao(form: dict) -> dict:
        # Mesma validação, mas sem obrigatoriedade de tipo (não pode mudar)
        erros = {}
        if not form.get("nome"):
            erros["nome"] = "Nome é obrigatório."
        try:
            preco = float(form["preco"])
            if preco <= 0:
                erros["preco"] = "Preço deve ser maior que zero."
        except (ValueError, KeyError):
            erros["preco"] = "Preço inválido."
        # Para edição, o tipo não muda, mas validamos se vier
        if "tipo" in form:
            tipo = form["tipo"]
            if tipo not in ("pronta_entrega", "encomenda"):
                erros["tipo"] = "Tipo inválido."
        # Validações condicionais conforme tipo (se vier)
        if form.get("tipo") == "pronta_entrega":
            try:
                qtd = int(form.get("quantidade_estoque", 0))
                if qtd < 0:
                    erros["quantidade_estoque"] = "Estoque não pode ser negativo."
            except ValueError:
                erros["quantidade_estoque"] = "Quantidade inválida."
        elif form.get("tipo") == "encomenda":
            try:
                prazo = int(form.get("prazo_entrega", 0))
                if prazo < 0:
                    erros["prazo_entrega"] = "Prazo inválido."
            except ValueError:
                erros["prazo_entrega"] = "Prazo inválido."
            try:
                taxa = float(form.get("taxa_extra", 0.0))
                if taxa < 0:
                    erros["taxa_extra"] = "Taxa extra inválida."
            except ValueError:
                erros["taxa_extra"] = "Taxa extra inválida."
        if not form.get("categoria"):
            erros["categoria"] = "Categoria é obrigatória."
        return erros