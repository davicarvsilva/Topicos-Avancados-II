import unittest
from entities.Mensagem import Mensagem
from entities.EnviadorEmail import EnviadorEmail
from entities.EnviadorSMS import EnviadorSMS

class TestMensagem(unittest.TestCase):
    def test_enviar_mensagem_email(self):
        enviador = EnviadorEmail()
        mensagem = Mensagem("Olá por e-mail!", enviador)
        self.assertEqual(mensagem.enviar_mensagem(), "Enviando e-mail: Olá por e-mail!")
    
    def test_enviar_mensagem_sms(self):
        enviador = EnviadorSMS()
        mensagem = Mensagem("Olá por SMS!", enviador)
        self.assertEqual(mensagem.enviar_mensagem(), "Enviando SMS: Olá por SMS!")


if __name__ == '__main__':
    unittest.main()