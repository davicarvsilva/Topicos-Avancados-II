from .InterfaceEnviador import InterfaceEnviador

class EnviadorSMS(InterfaceEnviador):
    def enviar(self, mensagem):
        # Lógica para enviar SMS
        return f"Enviando SMS: {mensagem}"