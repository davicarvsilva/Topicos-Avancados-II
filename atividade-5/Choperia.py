from entidades.OrdemServico import OrdemServico

class Choperia:
    def registrar_usuario(self, user, repositories):
        repositories.adicionar_user(user)

    def registrar_chopeira(self, chopeira, repositories):
        repositories.adicionar_chopeira(chopeira)

    def registrar_cilindro(self, cilindro, repositories):
        repositories.adicionar_cilindro(cilindro)

    def registrar_barril(self, barril, repositories):
        repositories.adicionar_barril(barril)

    def registrar_manometro(self, manometro, repositories):
        repositories.adicionar_manometro(manometro)

    def criar_ordem_servico(self, litros, kit_extracao, repositories):
        for barril in repositories.barris:
            if barril.litros == litros:
                try:
                    kit = repositories.gerar_kit_extracao()
                except Exception as e:  
                    print(e)
                    return 
                
                ordem_servico = OrdemServico(barril, kit)
                repositories.adicionar_ordem_servico(ordem_servico)
                return ordem_servico
