from werkzeug.security import generate_password_hash, check_password_hash

class Usuario:
    def __init__(self, id=None, nome=None, login=None, senha_hash=None):
        self.__id = id
        self.__nome = nome
        self.__login = login
        self.__senha_hash = senha_hash  # pode ser None inicialmente

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_login(self):
        return self.__login

    def get_senha_hash(self):
        return self.__senha_hash

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_login(self, login):
        self.__login = login

    def set_senha(self, senha):
        self.__senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        if self.__senha_hash is None:
            return False
        return check_password_hash(self.__senha_hash, senha)

    @staticmethod
    def autenticar(login, senha):
        from database.connection import get_connection   # <-- importa a função certa
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, login, senha_hash FROM usuarios WHERE login = ?", (login,))
        row = cursor.fetchone()
        if row:
            usuario = Usuario(id=row[0], nome=row[1], login=row[2], senha_hash=row[3])
            if usuario.verificar_senha(senha):
                return usuario
        return None