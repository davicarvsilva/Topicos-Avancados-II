import uuid

class OrdemServicoRepository:
    def __init__(self):
        self.ordens = []

    def gerar_uuid(self):
        return str(uuid.uuid4())

    def adicionar_ordem_servico(self, ordem_servico):
        ordem_servico.id = self.gerar_uuid()
        self.ordens.append(ordem_servico)

    def buscar_ordem_servico(self, ordem_id):
        for ordem in self.ordens:
            if ordem.id == ordem_id:
                return ordem
        return None

    def atualizar_ordem_servico(self, ordem_id, nova_ordem):
        ordem = self.buscar_ordem_servico(ordem_id)
        if ordem:
            ordem.barril = nova_ordem.barril
            ordem.kit = nova_ordem.kit
            return True
        return False

    def remover_ordem_servico(self, ordem_id):
        ordem = self.buscar_ordem_servico(ordem_id)
        if ordem:
            self.ordens.remove(ordem)
            return True
        return False

    def listar_ordens_servico(self):
        return self.ordens