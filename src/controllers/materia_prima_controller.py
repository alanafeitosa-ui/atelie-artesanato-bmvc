from database.connection import get_connection
from models.materiaPrima import MateriaPrima
from websocket import socketio

class MateriaPrimaController:

    @staticmethod
    def listar_todas():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM materia_prima")
        rows = cursor.fetchall()
        conn.close()
        return [MateriaPrima.from_row(row) for row in rows]

    @staticmethod
    def buscar_por_id(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM materia_prima WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return MateriaPrima.from_row(row)
        return None

    @staticmethod
    def criar(dados: dict):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO materia_prima (nome, unidade_medida, quantidade_estoque, estoque_minimo)
            VALUES (?, ?, ?, ?)
        """, (
            dados["nome"],
            dados["unidade_medida"],
            dados.get("quantidade_estoque", 0.0),
            dados.get("estoque_minimo", 0.0)
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
    def atualizar(materia_prima: MateriaPrima):
        """
        Recebe um objeto MateriaPrima (já modificado via setters) e persiste as alterações.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE materia_prima
            SET nome = ?,
                unidade_medida = ?,
                quantidade_estoque = ?,
                estoque_minimo = ?
            WHERE id = ?
        """, (
            materia_prima.get_nome(),
            materia_prima.get_unidade_medida(),
            materia_prima.get_quantidade_estoque(),
            materia_prima.get_estoque_minimo(),
            materia_prima.get_id()
        ))
        conn.commit()

        socketio.emit('estoque_atualizado', {
            'tipo': 'materia_prima',
            'id': materia_prima.get_id(),
            'estoque': materia_prima.get_quantidade_estoque()
        })

        conn.close()

    @staticmethod
    def excluir(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM materia_prima WHERE id = ?", (id,))
        conn.commit()

        socketio.emit('estoque_atualizado', {
            'tipo': 'materia_prima',
            'id': id,
            'estoque': 0  # matéria-prima removida
        })

        conn.close()