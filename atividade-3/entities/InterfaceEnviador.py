
from abc import ABC, abstractmethod

class InterfaceEnviador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass