from database.connection import get_connection
from models.pedido import Pedido
from models.item_pedido import ItemPedido

class PedidoController:
    @staticmethod
    def listar_todos():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedido")
        rows = cursor.fetchall()
        pedidos = []
        for row in rows:
            pedido = Pedido.from_row(row)
            cursor.execute("SELECT * FROM item_pedido WHERE pedido_id = ?", (pedido.get_id(),))
            itens_rows = cursor.fetchall()
            itens = [ItemPedido.from_row(item_row) for item_row in itens_rows]
            pedido.set_itens(itens)
            pedidos.append(pedido)
        conn.close()
        return pedidos

    @staticmethod
    def buscar_por_id(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedido WHERE id = ?", (id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None
        pedido = Pedido.from_row(row)
        cursor.execute("SELECT * FROM item_pedido WHERE pedido_id = ?", (id,))
        itens_rows = cursor.fetchall()
        itens = [ItemPedido.from_row(item_row) for item_row in itens_rows]
        pedido.set_itens(itens)
        conn.close()
        return pedido

    @staticmethod
    def criar(dados: dict):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedido (cliente_id, status) VALUES (?, 'Pendente')",
                       (dados["cliente_id"],))
        pedido_id = cursor.lastrowid
        for item in dados["itens"]:
            cursor.execute("INSERT INTO item_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
                           (pedido_id, item["produto_id"], item["quantidade"], item["preco_unitario"]))
        cursor.execute("""
            UPDATE pedido SET valor_total = (
                SELECT SUM(quantidade * preco_unitario) FROM item_pedido WHERE pedido_id = ?
            ) WHERE id = ?
        """, (pedido_id, pedido_id))
        conn.commit()
        conn.close()
        return pedido_id

    @staticmethod
    def atualizar(pedido: Pedido, itens: list = None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE pedido SET status = ? WHERE id = ?",
                       (pedido.get_status(), pedido.get_id()))
        if itens is not None:
            cursor.execute("DELETE FROM item_pedido WHERE pedido_id = ?", (pedido.get_id(),))
            for item in itens:
                cursor.execute("INSERT INTO item_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
                               (pedido.get_id(), item["produto_id"], item["quantidade"], item["preco_unitario"]))
            cursor.execute("""
                UPDATE pedido SET valor_total = (
                    SELECT SUM(quantidade * preco_unitario) FROM item_pedido WHERE pedido_id = ?
                ) WHERE id = ?
            """, (pedido.get_id(), pedido.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM item_pedido WHERE pedido_id = ?", (id,))
        cursor.execute("DELETE FROM pedido WHERE id = ?", (id,))
        conn.commit()
        conn.close()