import uuid

class Repositories:
    users = []
    chopeiras = []
    cilindros = []
    manometros = []
    barris = []
    ordens_servico = []

    def adicionar_user(self, user):
        try: 
            self.verificar_login_valido(user)
        except Exception as e:
            print(e)
            return 

        user.id = self.gerar_uuid()       
        self.users.append(user) 

    def adicionar_chopeira(self, chopeira):
        chopeira.id = self.gerar_uuid()       
        self.chopeiras.append(chopeira) 

    def adicionar_barril(self, barril):
        barril.id = self.gerar_uuid()       
        self.barris.append(barril) 

    def adicionar_cilindro(self, cilindro):
        cilindro.id = self.gerar_uuid()       
        self.cilindros.append(cilindro) 

    def adicionar_manometro(self, manometro):
        manometro.id = self.gerar_uuid()       
        self.manometros.append(manometro)

    def adicionar_ordem_servico(self, ordem_servico):
        ordem_servico.id = self.gerar_uuid()       
        self.ordens_servico.append(ordem_servico)  

    def verificar_login_valido(self, user):
        for user_salvo in self.users:
            if user_salvo.login == user.login:
                raise ValueError("Login já existe")

    def gerar_kit_extracao(self):
        chopeira_os = ''
        manometro_os = ''
        cilindro_os = ''

        for chopeira in self.chopeiras:
            if chopeira.status == "disponivel":
                chopeira_os = chopeira 
                break

        for cilindro in self.cilindros:
            if cilindro.status == "disponivel":
                cilindro_os = cilindro
                break

        for manometro in self.manometros:
            if manometro.status == "disponivel":
                manometro_os = manometro
                break

        if manometro_os and cilindro_os and chopeira_os:
            chopeira_os.status = "ocupado"
            cilindro_os.status = "ocupado"
            manometro_os.status = "ocupado" 

            return {'chopeira': chopeira_os, 'cilindro': cilindro_os, 'manometro': manometro_os}
        else:
            raise ValueError("Não há materiais para extração disponíveis")

    def gerar_uuid(self):
       return uuid.uuid4()