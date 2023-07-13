import uuid
import hashlib

class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def gerar_uuid(self):
        return str(uuid.uuid4())

    def adicionar_usuario(self, usuario):
        usuario.id = self.gerar_uuid()
        self.usuarios.append(usuario)

    def buscar_usuario(self, usuario_id):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

    def autenticar_usuario(self, login, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for usuario in self.usuarios:
            if usuario.login == login and usuario.password == hashed_password:
                return usuario
        return None

    def remover_usuario(self, usuario_id):
        usuario = self.buscar_usuario(usuario_id)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

    def listar_usuarios(self):
        return self.usuarios
