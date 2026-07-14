from database.connection import get_connection
from models.produto import Produto, ProdutoProntaEntrega, ProdutoEncomenda
from websocket import socketio

class ProdutoController:

    @staticmethod
    def listar_todos():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produto WHERE ativo = 1")
        rows = cursor.fetchall()
        conn.close()
        return [Produto.from_row(row) for row in rows]

    @staticmethod
    def buscar_por_id(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produto WHERE id = ? AND ativo = 1", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Produto.from_row(row)
        return None

    @staticmethod
    def criar(dados: dict):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO produto (nome, preco, categoria, tipo, quantidade_estoque, prazo_entrega, taxa_extra)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            dados["nome"],
            dados["preco"],
            dados["categoria"],
            dados["tipo"],
            dados.get("quantidade_estoque", 0),
            dados.get("prazo_entrega", 0),
            dados.get("taxa_extra", 0.0)
        ))
        conn.commit()
        novo_id = cursor.lastrowid

        socketio.emit('estoque_atualizado', {
            'tipo': 'materia_prima',
            'id': novo_id,
            'estoque': dados.get("quantidade_estoque", 0.0)
        })

        conn.close()
        return novo_id

    @staticmethod
    def atualizar(produto):
        """
        Recebe um objeto Produto (já modificado) e persiste as alterações no banco.
        """
        conn = get_connection()
        cursor = conn.cursor()
        if isinstance(produto, ProdutoProntaEntrega):
            cursor.execute("""
                UPDATE produto 
                SET nome = ?, preco = ?, categoria = ?, tipo = ?,
                    quantidade_estoque = ?
                WHERE id = ?
            """, (
                produto.get_nome(),
                produto.get_preco(),
                produto.get_categoria(),
                'pronta_entrega',
                produto.get_quantidade_estoque(),
                produto.get_id()
            ))
        elif isinstance(produto, ProdutoEncomenda):
            cursor.execute("""
                UPDATE produto 
                SET nome = ?, preco = ?, categoria = ?, tipo = ?,
                    prazo_entrega = ?, taxa_extra = ?
                WHERE id = ?
            """, (
                produto.get_nome(),
                produto.get_preco(),
                produto.get_categoria(),
                'encomenda',
                produto.get_prazo_entrega(),
                produto.get_taxa_extra(),
                produto.get_id()
            ))
        else:
            raise TypeError("Tipo de produto não suportado para atualização.")
        conn.commit()
        if isinstance(produto, ProdutoProntaEntrega):
            socketio.emit('estoque_atualizado', {
                'tipo': 'produto',
                'id': produto.get_id(),
                'estoque': produto.get_quantidade_estoque()
            })

        conn.close()

    @staticmethod
    def excluir(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE produto SET ativo = 0 WHERE id = ?", (id,))
        conn.commit()
        # Opcional: emitir que o produto foi removido (estoque zero)
        socketio.emit('estoque_atualizado', {
            'tipo': 'produto',
            'id': id,
            'estoque': 0  # não existe mais no ativo
        })
        conn.close()