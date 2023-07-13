import unittest
from repositories.BarrilRepository import BarrilRepository
from repositories.ChopeiraRepository import ChopeiraRepository 
from repositories.CilindroRepository import CilindroRepository
from repositories.ManometroRepository import ManometroRepository
from repositories.OrdemServicoRepository import OrdemServicoRepository
from repositories.UsuarioRepository import UsuarioRepository  

from entidades.Barril import Barril
from entidades.Chopeira import Chopeira
from entidades.Cilindro import Cilindro
from entidades.Manometro import Manometro
from entidades.OrdemServico import OrdemServico
from entidades.Usuario import Usuario


class TestRepositories(unittest.TestCase):
    def setUp(self):
        self.barril_repository = BarrilRepository()
        self.chopeira_repository = ChopeiraRepository()
        self.cilindro_repository = CilindroRepository()
        self.manometro_repository = ManometroRepository()
        self.ordem_servico_repository = OrdemServicoRepository()
        self.usuario_repository = UsuarioRepository()

    def test_barril_repository(self):
        barril = Barril(10.99, 5.0, 100, "Tipo A")

        # Test adding a barrel
        self.barril_repository.adicionar_barril(barril)
        self.assertEqual(len(self.barril_repository.barris), 1)

        # Test searching for a barrel
        found_barril = self.barril_repository.buscar_barril(barril.id)
        self.assertEqual(found_barril, barril)

        # Test updating a barrel
        novo_barril = Barril(12.99, 6.0, 120, "Tipo B")
        self.barril_repository.atualizar_barril(barril.id, novo_barril)
        updated_barril = self.barril_repository.buscar_barril(barril.id)
        self.assertEqual(updated_barril.preco, novo_barril.preco)
        self.assertEqual(updated_barril.peso, novo_barril.peso)
        self.assertEqual(updated_barril.litros, novo_barril.litros)
        self.assertEqual(updated_barril.tipo, novo_barril.tipo)

        # Test removing a barrel
        self.barril_repository.remover_barril(barril.id)
        self.assertEqual(len(self.barril_repository.barris), 0)

    def test_chopeira_repository(self):
        chopeira = Chopeira("220V", 299.99, "Ativa", "Prata")

        # Test adding a chopeira
        self.chopeira_repository.adicionar_chopeira(chopeira)
        self.assertEqual(len(self.chopeira_repository.chopeiras), 1)

        # Test searching for a chopeira
        found_chopeira = self.chopeira_repository.buscar_chopeira(chopeira.id)
        self.assertEqual(found_chopeira, chopeira)

        # Test updating a chopeira
        nova_chopeira = Chopeira("110V", 349.99, "Inativa", "Preto")
        self.chopeira_repository.atualizar_chopeira(chopeira.id, nova_chopeira)
        updated_chopeira = self.chopeira_repository.buscar_chopeira(chopeira.id)
        self.assertEqual(updated_chopeira.voltagem, nova_chopeira.voltagem)
        self.assertEqual(updated_chopeira.preco, nova_chopeira.preco)
        self.assertEqual(updated_chopeira.status, nova_chopeira.status)
        self.assertEqual(updated_chopeira.cor, nova_chopeira.cor)

        # Test removing a chopeira
        self.chopeira_repository.remover_chopeira(chopeira.id)
        self.assertEqual(len(self.chopeira_repository.chopeiras), 0)

    def test_cilindro_repository(self):
        cilindro = Cilindro("Prata", 10.5, "Disponível")

        # Test adding a cilindro
        self.cilindro_repository.adicionar_cilindro(cilindro)
        self.assertEqual(len(self.cilindro_repository.cilindros), 1)

        # Test searching for a cilindro
        found_cilindro = self.cilindro_repository.buscar_cilindro(cilindro.id)
        self.assertEqual(found_cilindro, cilindro)

        # Test updating a cilindro
        novo_cilindro = Cilindro("Preto", 15.2, "Indisponível")
        self.cilindro_repository.atualizar_cilindro(cilindro.id, novo_cilindro)
        updated_cilindro = self.cilindro_repository.buscar_cilindro(cilindro.id)
        self.assertEqual(updated_cilindro.cor, novo_cilindro.cor)
        self.assertEqual(updated_cilindro.peso, novo_cilindro.peso)
        self.assertEqual(updated_cilindro.status, novo_cilindro.status)

        # Test removing a cilindro
        self.cilindro_repository.remover_cilindro(cilindro.id)
        self.assertEqual(len(self.cilindro_repository.cilindros), 0)

    def test_manometro_repository(self):
        manometro = Manometro("Alta", "Ativo")

        # Test adding a manometro
        self.manometro_repository.adicionar_manometro(manometro)
        self.assertEqual(len(self.manometro_repository.manometros), 1)

        # Test searching for a manometro
        found_manometro = self.manometro_repository.buscar_manometro(manometro.id)
        self.assertEqual(found_manometro, manometro)

        # Test updating a manometro
        novo_manometro = Manometro("Baixa", "Inativo")
        self.manometro_repository.atualizar_manometro(manometro.id, novo_manometro)
        updated_manometro = self.manometro_repository.buscar_manometro(manometro.id)
        self.assertEqual(updated_manometro.regulacao, novo_manometro.regulacao)
        self.assertEqual(updated_manometro.status, novo_manometro.status)

        # Test removing a manometro
        self.manometro_repository.remover_manometro(manometro.id)
        self.assertEqual(len(self.manometro_repository.manometros), 0)

    def test_ordem_servico_repository(self):
        barril = Barril(10.99, 5.0, 100, "Tipo A")
        kit = ["Item 1", "Item 2"]
        ordem_servico = OrdemServico(barril, kit)

        # Test adding an ordem_servico
        self.ordem_servico_repository.adicionar_ordem_servico(ordem_servico)
        self.assertEqual(len(self.ordem_servico_repository.ordens), 1)

        # Test searching for an ordem_servico
        found_ordem_servico = self.ordem_servico_repository.buscar_ordem_servico(ordem_servico.id)
        self.assertEqual(found_ordem_servico, ordem_servico)

        # Test updating an ordem_servico
        novo_barril = Barril(12.99, 6.0, 120, "Tipo B")
        novo_kit = ["Item 3", "Item 4"]
        nova_ordem_servico = OrdemServico(novo_barril, novo_kit)
        self.ordem_servico_repository.atualizar_ordem_servico(ordem_servico.id, nova_ordem_servico)
        updated_ordem_servico = self.ordem_servico_repository.buscar_ordem_servico(ordem_servico.id)
        self.assertEqual(updated_ordem_servico.barril, novo_barril)
        self.assertEqual(updated_ordem_servico.kit, novo_kit)

        # Test removing an ordem_servico
        self.ordem_servico_repository.remover_ordem_servico(ordem_servico.id)
        self.assertEqual(len(self.ordem_servico_repository.ordens), 0)

    def test_usuario_repository(self):
        usuario = Usuario("admin", "password123")

        # Test adding a usuario
        self.usuario_repository.adicionar_usuario(usuario)
        self.assertEqual(len(self.usuario_repository.usuarios), 1)

        # Test authenticating a usuario
        authenticated_usuario = self.usuario_repository.autenticar_usuario(usuario.login, "password123")
        self.assertEqual(authenticated_usuario, usuario)

        # Test removing a usuario
        self.usuario_repository.remover_usuario(usuario.id)
        self.assertEqual(len(self.usuario_repository.usuarios), 0)

if __name__ == '__main__':
    unittest.main()
