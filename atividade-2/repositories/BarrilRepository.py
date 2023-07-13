import uuid

class BarrilRepository:
    def __init__(self):
        self.barris = []

    def gerar_uuid(self):
        return str(uuid.uuid4())

    def adicionar_barril(self, barril):
        barril.id = self.gerar_uuid()
        self.barris.append(barril)

    def buscar_barril(self, barril_id):
        for barril in self.barris:
            if barril.id == barril_id:
                return barril
        return None

    def atualizar_barril(self, barril_id, novo_barril):
        barril = self.buscar_barril(barril_id)
        if barril:
            barril.preco = novo_barril.preco
            barril.peso = novo_barril.peso
            barril.litros = novo_barril.litros
            barril.tipo = novo_barril.tipo
            return True
        return False

    def remover_barril(self, barril_id):
        barril = self.buscar_barril(barril_id)
        if barril:
            self.barris.remove(barril)
            return True
        return False

    def listar_barris(self):
        return self.barris