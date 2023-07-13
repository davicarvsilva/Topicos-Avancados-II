import uuid

class CilindroRepository:
    def __init__(self):
        self.cilindros = []

    def gerar_uuid(self):
        return str(uuid.uuid4())

    def adicionar_cilindro(self, cilindro):
        cilindro.id = self.gerar_uuid()
        self.cilindros.append(cilindro)

    def buscar_cilindro(self, cilindro_id):
        for cilindro in self.cilindros:
            if cilindro.id == cilindro_id:
                return cilindro
        return None

    def atualizar_cilindro(self, cilindro_id, novo_cilindro):
        cilindro = self.buscar_cilindro(cilindro_id)
        if cilindro:
            cilindro.cor = novo_cilindro.cor
            cilindro.peso = novo_cilindro.peso
            cilindro.status = novo_cilindro.status
            return True
        return False

    def remover_cilindro(self, cilindro_id):
        cilindro = self.buscar_cilindro(cilindro_id)
        if cilindro:
            self.cilindros.remove(cilindro)
            return True
        return False

    def listar_cilindros(self):
        return self.cilindros