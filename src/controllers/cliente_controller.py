from database.connection import get_connection
from models.cliente import Cliente

class ClienteController:
    @staticmethod
    def listar_todos():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cliente")
        rows = cursor.fetchall()
        conn.close()
        return [Cliente.from_row(row) for row in rows]

    @staticmethod
    def buscar_por_id(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return Cliente.from_row(row) if row else None

    @staticmethod
    def criar(dados: dict):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cliente (nome, telefone, email, endereco)
            VALUES (?, ?, ?, ?)
        """, (dados["nome"], dados.get("telefone"), dados.get("email"), dados.get("endereco")))
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return novo_id

    @staticmethod
    def atualizar(cliente: Cliente):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cliente SET nome=?, telefone=?, email=?, endereco=?
            WHERE id=?
        """, (cliente.get_nome(), cliente.get_telefone(), cliente.get_email(), cliente.get_endereco(), cliente.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE id = ?", (id,))
        conn.commit()
        conn.close()