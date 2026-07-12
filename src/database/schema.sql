PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    endereco TEXT
);
CREATE TABLE IF NOT EXISTS produto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    tipo TEXT NOT NULL
        CHECK(tipo IN ('pronta_entrega', 'encomenda')),
    quantidade_estoque INTEGER DEFAULT 0,
    prazo_producao INTEGER,
    ativo INTEGER DEFAULT 1
);
CREATE TABLE IF NOT EXISTS materia_prima(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    unidade_medida TEXT NOT NULL,
    quantidade_estoque REAL DEFAULT 0,
    estoque_minimo REAL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS produto_materia_prima (
    produto_id INTEGER NOT NULL,
    materia_prima_id INTEGER NOT NULL,
    quantidade_utilizada REAL NOT NULL,
    PRIMARY KEY(produto_id, materia_prima_id),
    FOREIGN KEY(produto_id) REFERENCES produto(id) ON DELETE CASCADE,
    FOREIGN KEY(materia_prima_id) REFERENCES materia_prima(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS pedido(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGERNOT NULL,
    data_pedido TEXT DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'Pendente' CHECK(status IN(
        'Pendente',
        'Em produção',
        'Finalizado',
        'Entregue',
        'Cancelado'
    )),
    valor_total REAL DEFAULT 0,
    FOREIGN KEY(cliente_id) REFERENCES cliente(id)
);
CREATE TABLE IF NOT EXISTS item_pedido(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY(pedido_id) REFERENCES pedido(id) ON DELETE CASCADE,
    FOREIGN KEY(produto_id) REFERENCES produto(id)
);