class Mensagem:
    def __init__(self, conteudo, enviador):
        self.conteudo = conteudo
        self.enviador = enviador
    
    def enviar_mensagem(self):
        return self.enviador.enviar(self.conteudo)