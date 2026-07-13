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

@app.route("/pedidos")
def listar_pedidos():
    try:
        from controllers.pedido_controller import PedidoController
        pedidos = PedidoController.listar_todos()
    except Exception:
        pedidos = []
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/pedidos/criar", methods=["GET", "POST"])
def criar_pedido():
    if request.method == "POST":
        return redirect(url_for("listar_pedidos"))
    try:
        from controllers.cliente_controller import ClienteController
        clientes = ClienteController.listar_todos()
    except Exception:
        clientes = []
    try:
        from controllers.produto_controller import ProdutoController
        produtos = ProdutoController.listar_todos()
    except Exception:
        produtos = []
    return render_template("form_pedido.html", erros={}, dados={}, clientes=clientes, produtos=produtos, itens=[])

@app.route("/pedidos/editar/<int:id>", methods=["GET", "POST"])
def editar_pedido(id):
    if request.method == "POST":
        return redirect(url_for("listar_pedidos"))
    try:
        from controllers.cliente_controller import ClienteController
        clientes = ClienteController.listar_todos()
    except Exception:
        clientes = []
    try:
        from controllers.produto_controller import ProdutoController
        produtos = ProdutoController.listar_todos()
    except Exception:
        produtos = []
    pedido_ficticio = {"get_id": lambda: id, "get_status": lambda: "Pendente", "get_data_pedido": lambda: "", "get_valor_total": lambda: 0.0, "get_cliente": lambda: None}
    return render_template("form_pedido.html", erros={}, dados={}, pedido=pedido_ficticio, clientes=clientes, produtos=produtos, itens=[])

@app.route("/clientes")
def listar_clientes():
    try:
        from controllers.cliente_controller import ClienteController
        clientes = ClienteController.listar_todos()
    except Exception:
        clientes = []
    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes/criar", methods=["GET", "POST"])
def criar_cliente():
    if request.method == "POST":
        return redirect(url_for("listar_clientes"))
    return render_template("form_cliente.html", erros={}, dados={})

@app.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    if request.method == "POST":
        return redirect(url_for("listar_clientes"))
    dados = {"nome": "Cliente Exemplo", "email": "", "telefone": "", "endereco": ""}
    return render_template("form_cliente.html", erros={}, dados=dados, cliente={"get_id": lambda: id})

if __name__ == "__main__":
    app.run(debug=True)