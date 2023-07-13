import uuid

class ManometroRepository:
    def __init__(self):
        self.manometros = []

    def gerar_uuid(self):
        return str(uuid.uuid4())

    def adicionar_manometro(self, manometro):
        manometro.id = self.gerar_uuid()
        self.manometros.append(manometro)

    def buscar_manometro(self, manometro_id):
        for manometro in self.manometros:
            if manometro.id == manometro_id:
                return manometro
        return None

    def atualizar_manometro(self, manometro_id, novo_manometro):
        manometro = self.buscar_manometro(manometro_id)
        if manometro:
            manometro.regulacao = novo_manometro.regulacao
            manometro.status = novo_manometro.status
            return True
        return False

    def remover_manometro(self, manometro_id):
        manometro = self.buscar_manometro(manometro_id)
        if manometro:
            self.manometros.remove(manometro)
            return True
        return False

    def listar_manometros(self):
        return self.manometros