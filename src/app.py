from flask import Flask, render_template, request, redirect, url_for
from controllers.produto_controller import ProdutoController
from controllers.materia_prima_controller import MateriaPrimaController
from boundary.produto_boundary import ProdutoBoundary
from boundary.materia_prima_boundary import MateriaPrimaBoundary
from models.produto import ProdutoProntaEntrega, ProdutoEncomenda

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login")
def login():
    return "Login em construção"
@app.route("/produtos")
def listar_produtos():
    produtos = ProdutoController.listar_todos()
    return render_template("produtos.html", produtos=produtos)

@app.route("/produtos/criar", methods=["GET", "POST"])
def criar_produto():
    if request.method == "POST":
        dados = request.form.to_dict()
        erros = ProdutoBoundary.validar_criacao(dados)
        if not erros:
            ProdutoController.criar(dados)
            return redirect(url_for("listar_produtos"))
        return render_template("form_produto.html", erros=erros, dados=dados)
    return render_template("form_produto.html", erros={}, dados={})

@app.route("/produtos/editar/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    produto = ProdutoController.buscar_por_id(id)
    if not produto:
        return "Produto não encontrado", 404
    if request.method == "POST":
        dados = request.form.to_dict()
        erros = ProdutoBoundary.validar_edicao(dados)
        if not erros:
            produto.set_nome(dados["nome"])
            produto.set_preco(float(dados["preco"]))
            produto.set_categoria(dados["categoria"])
            if isinstance(produto, ProdutoProntaEntrega):
                produto.set_quantidade_estoque(int(dados.get("quantidade_estoque", 0)))
            elif isinstance(produto, ProdutoEncomenda):
                produto.set_prazo_entrega(int(dados.get("prazo_entrega", 0)))
                produto.set_taxa_extra(float(dados.get("taxa_extra", 0.0)))
            ProdutoController.atualizar(produto)
            return redirect(url_for("listar_produtos"))
        return render_template("form_produto.html", erros=erros, dados=dados, produto=produto)
    # GET: preenche formulário com dados atuais
    dados_iniciais = {
        "nome": produto.get_nome(),
        "preco": produto.get_preco(),
        "categoria": produto.get_categoria(),
        "tipo": "pronta_entrega" if isinstance(produto, ProdutoProntaEntrega) else "encomenda"
    }
    if isinstance(produto, ProdutoProntaEntrega):
        dados_iniciais["quantidade_estoque"] = produto.get_quantidade_estoque()
    else:
        dados_iniciais["prazo_entrega"] = produto.get_prazo_entrega()
        dados_iniciais["taxa_extra"] = produto.get_taxa_extra()
    return render_template("form_produto.html", erros={}, dados=dados_iniciais, produto=produto)

@app.route("/produtos/excluir/<int:id>")
def excluir_produto(id):
    ProdutoController.excluir(id)
    return redirect(url_for("listar_produtos"))

@app.route("/materias_primas")
def listar_materias_primas():
    materias = MateriaPrimaController.listar_todas()
    return render_template("materias_primas.html", materias=materias)

@app.route("/materias_primas/criar", methods=["GET", "POST"])
def criar_materia_prima():
    if request.method == "POST":
        dados = request.form.to_dict()
        erros = MateriaPrimaBoundary.validar_criacao(dados)
        if not erros:
            MateriaPrimaController.criar(dados)
            return redirect(url_for("listar_materias_primas"))
        return render_template("form_materia_prima.html", erros=erros, dados=dados)
    return render_template("form_materia_prima.html", erros={}, dados={})

@app.route("/materias_primas/editar/<int:id>", methods=["GET", "POST"])
def editar_materia_prima(id):
    materia = MateriaPrimaController.buscar_por_id(id)
    if not materia:
        return "Matéria-prima não encontrada", 404
    if request.method == "POST":
        dados = request.form.to_dict()
        erros = MateriaPrimaBoundary.validar_edicao(dados)
        if not erros:
            materia.set_nome(dados["nome"])
            materia.set_unidade_medida(dados["unidade_medida"])
            materia.set_quantidade_estoque(float(dados["quantidade_estoque"]))
            materia.set_estoque_minimo(float(dados["estoque_minimo"]))
            MateriaPrimaController.atualizar(materia)
            return redirect(url_for("listar_materias_primas"))
        return render_template("form_materia_prima.html", erros=erros, dados=dados, materia=materia)
    dados_iniciais = {
        "nome": materia.get_nome(),
        "unidade_medida": materia.get_unidade_medida(),
        "quantidade_estoque": materia.get_quantidade_estoque(),
        "estoque_minimo": materia.get_estoque_minimo()
    }
    return render_template("form_materia_prima.html", erros={}, dados=dados_iniciais, materia=materia)

@app.route("/materias_primas/excluir/<int:id>")
def excluir_materia_prima(id):
    from controllers.materia_prima_controller import MateriaPrimaController
    MateriaPrimaController.excluir(id)
    return redirect(url_for("listar_materias_primas"))

# ---------- CLIENTES ----------
@app.route("/clientes")
def listar_clientes():
    from controllers.cliente_controller import ClienteController
    clientes = ClienteController.listar_todos()
    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes/criar", methods=["GET", "POST"])
def criar_cliente():
    from controllers.cliente_controller import ClienteController
    from boundary.cliente_boundary import ClienteBoundary
    if request.method == "POST":
        dados = request.form.to_dict()
        erros = ClienteBoundary.validar_criacao(dados)
        if not erros:
            ClienteController.criar(dados)
            return redirect(url_for("listar_clientes"))
        return render_template("form_cliente.html", erros=erros, dados=dados)
    return render_template("form_cliente.html", erros={}, dados={})

@app.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    from controllers.cliente_controller import ClienteController
    from boundary.cliente_boundary import ClienteBoundary
    cliente = ClienteController.buscar_por_id(id)
    if not cliente:
        return "Cliente não encontrado", 404
    if request.method == "POST":
        dados = request.form.to_dict()
        erros = ClienteBoundary.validar_edicao(dados)
        if not erros:
            cliente.set_nome(dados["nome"])
            cliente.set_telefone(dados.get("telefone", ""))
            cliente.set_email(dados.get("email", ""))
            cliente.set_endereco(dados.get("endereco", ""))
            ClienteController.atualizar(cliente)
            return redirect(url_for("listar_clientes"))
        return render_template("form_cliente.html", erros=erros, dados=dados, cliente=cliente)
    dados_iniciais = {
        "nome": cliente.get_nome(),
        "telefone": cliente.get_telefone(),
        "email": cliente.get_email(),
        "endereco": cliente.get_endereco()
    }
    return render_template("form_cliente.html", erros={}, dados=dados_iniciais, cliente=cliente)

@app.route("/clientes/excluir/<int:id>")
def excluir_cliente(id):
    from controllers.cliente_controller import ClienteController
    ClienteController.excluir(id)
    return redirect(url_for("listar_clientes"))

# ---------- PEDIDOS ----------
@app.route("/pedidos")
def listar_pedidos():
    from controllers.pedido_controller import PedidoController
    pedidos = PedidoController.listar_todos()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/pedidos/criar", methods=["GET", "POST"])
def criar_pedido():
    from controllers.pedido_controller import PedidoController
    from controllers.cliente_controller import ClienteController
    from controllers.produto_controller import ProdutoController
    from boundary.pedido_boundary import PedidoBoundary
    if request.method == "POST":
        dados = request.form.to_dict()
        # Listas de itens
        produtos_ids = request.form.getlist("produto_id[]")
        quantidades = request.form.getlist("quantidade[]")
        precos = request.form.getlist("preco_unitario[]")
        itens = []
        for pid, qtd, prc in zip(produtos_ids, quantidades, precos):
            itens.append({"produto_id": int(pid), "quantidade": int(qtd), "preco_unitario": float(prc)})
        dados["itens"] = itens
        erros = PedidoBoundary.validar_criacao(dados)
        if not erros:
            PedidoController.criar(dados)
            return redirect(url_for("listar_pedidos"))
        clientes = ClienteController.listar_todos()
        produtos = ProdutoController.listar_todos()
        return render_template("form_pedido.html", erros=erros, dados=dados,
                               clientes=clientes, produtos=produtos, itens=itens)
    clientes = ClienteController.listar_todos()
    produtos = ProdutoController.listar_todos()
    return render_template("form_pedido.html", erros={}, dados={},
                           clientes=clientes, produtos=produtos, itens=[])

@app.route("/pedidos/editar/<int:id>", methods=["GET", "POST"])
def editar_pedido(id):
    from controllers.pedido_controller import PedidoController
    from controllers.cliente_controller import ClienteController
    from controllers.produto_controller import ProdutoController
    from boundary.pedido_boundary import PedidoBoundary
    pedido = PedidoController.buscar_por_id(id)
    if not pedido:
        return "Pedido não encontrado", 404
    if request.method == "POST":
        dados = request.form.to_dict()
        produtos_ids = request.form.getlist("produto_id[]")
        quantidades = request.form.getlist("quantidade[]")
        precos = request.form.getlist("preco_unitario[]")
        itens = []
        for pid, qtd, prc in zip(produtos_ids, quantidades, precos):
            itens.append({"produto_id": int(pid), "quantidade": int(qtd), "preco_unitario": float(prc)})
        dados["itens"] = itens
        erros = PedidoBoundary.validar_edicao(dados)
        if not erros:
            pedido.set_status(dados.get("status", pedido.get_status()))
            PedidoController.atualizar(pedido, itens)
            return redirect(url_for("listar_pedidos"))
        clientes = ClienteController.listar_todos()
        produtos = ProdutoController.listar_todos()
        return render_template("form_pedido.html", erros=erros, dados=dados,
                               pedido=pedido, clientes=clientes, produtos=produtos, itens=itens)
    # GET: preencher dados atuais
    clientes = ClienteController.listar_todos()
    produtos = ProdutoController.listar_todos()
    itens_formatados = []
    for item in pedido.get_itens():
        itens_formatados.append({
            "produto_id": item.get_produto_id(),
            "quantidade": item.get_quantidade(),
            "preco_unitario": item.get_preco_unitario()
        })
    dados = {"cliente_id": pedido.get_cliente_id(), "status": pedido.get_status()}
    return render_template("form_pedido.html", erros={}, dados=dados,
                           pedido=pedido, clientes=clientes, produtos=produtos, itens=itens_formatados)

@app.route("/pedidos/excluir/<int:id>")
def excluir_pedido(id):
    from controllers.pedido_controller import PedidoController
    PedidoController.excluir(id)
    return redirect(url_for("listar_pedidos"))

if __name__ == "__main__":
    app.run(debug=True)