import unittest

from Choperia import Choperia
from Repositories import Repositories
from entidades.Usuario import Usuario
from entidades.Chopeira import Chopeira
from entidades.Cilindro import Cilindro
from entidades.Barril import Barril
from entidades.Manometro import Manometro

class TestChoperia(unittest.TestCase):
    def setUp(self):
        self.choperia = Choperia()
        self.repositories = Repositories()

    def test_registrar_usuario(self):
        login = "davi"
        password = "123"
        usuario = Usuario(login, password)

        self.choperia.registrar_usuario(usuario, self.repositories)
        self.assertIn(usuario, self.repositories.users)

    def test_adicionar_chopeira(self):
        voltagem = "127"
        preco = 4233.59
        status = "disponivel"
        cor = "vermelho"

        chopeira = Chopeira(voltagem, preco, status, cor)
        
        self.choperia.registrar_chopeira(chopeira, self.repositories)
        self.assertIn(chopeira, self.repositories.chopeiras)

    def test_adicionar_cilindro(self):
        cor = "prata"
        peso = "4kg"
        status = "disponivel"

        cilindro = Cilindro(cor, peso, status)
        
        self.choperia.registrar_cilindro(cilindro, self.repositories)
        self.assertIn(cilindro, self.repositories.cilindros)

    def test_adicionar_barril(self):
        preco = 564.99
        peso = "40kg"
        litros = 30
        tipo = "Brahma"

        barril = Barril(preco, peso, litros, tipo)
        
        self.choperia.registrar_barril(barril, self.repositories)
        self.assertIn(barril, self.repositories.barris)

    def test_adicionar_manometro(self):
        regulacao = 3.6
        status = "disponivel"

        manometro = Manometro(regulacao, status)
        
        self.choperia.registrar_manometro(manometro, self.repositories)
        self.assertIn(manometro, self.repositories.manometros)
    
    def test_criar_ordem_servico(self):
        litros = 30
        kit_extracao = True

        ordem_servico = self.choperia.criar_ordem_servico(litros, kit_extracao, self.repositories)
        
        self.assertIn(ordem_servico, self.repositories.ordens_servico)

        # verifica se status da chopeira da OS é igual ao status da chopeira dos repositórios
        self.assertEqual(ordem_servico.kit['chopeira'].status, 
            next((chopeira for chopeira in self.repositories.chopeiras if ordem_servico.kit['chopeira'].id == chopeira.id), None).status)

        # verifica se status do cilindro da OS é igual ao status do cilindro dos repositórios
        self.assertEqual(ordem_servico.kit['cilindro'].status, 
            next((cilindro for cilindro in self.repositories.cilindros if ordem_servico.kit['cilindro'].id == cilindro.id), None).status)

        # verifica se status do manometro da OS é igual ao status do manometro dos repositórios
        self.assertEqual(ordem_servico.kit['manometro'].status, 
            next((manometro for manometro in self.repositories.manometros if ordem_servico.kit['manometro'].id == manometro.id), None).status)


if __name__ == '__main__':
    unittest.main()