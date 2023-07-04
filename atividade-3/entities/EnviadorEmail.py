from .InterfaceEnviador import InterfaceEnviador

class EnviadorEmail(InterfaceEnviador):
    def enviar(self, mensagem):
        # Lógica para enviar e-mail
        return f"Enviando e-mail: {mensagem}"