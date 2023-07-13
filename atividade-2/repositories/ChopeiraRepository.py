import uuid

class ChopeiraRepository:
    def __init__(self):
        self.chopeiras = []

    def gerar_uuid(self):
        return str(uuid.uuid4())

    def adicionar_chopeira(self, chopeira):
        chopeira.id = self.gerar_uuid()
        self.chopeiras.append(chopeira)

    def buscar_chopeira(self, chopeira_id):
        for chopeira in self.chopeiras:
            if chopeira.id == chopeira_id:
                return chopeira
        return None

    def atualizar_chopeira(self, chopeira_id, nova_chopeira):
        chopeira = self.buscar_chopeira(chopeira_id)
        if chopeira:
            chopeira.voltagem = nova_chopeira.voltagem
            chopeira.preco = nova_chopeira.preco
            chopeira.status = nova_chopeira.status
            chopeira.cor = nova_chopeira.cor
            return True
        return False

    def remover_chopeira(self, chopeira_id):
        chopeira = self.buscar_chopeira(chopeira_id)
        if chopeira:
            self.chopeiras.remove(chopeira)
            return True
        return False

    def listar_chopeiras(self):
        return self.chopeiras