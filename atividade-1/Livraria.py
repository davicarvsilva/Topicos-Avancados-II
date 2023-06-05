"""
Uma livraria contém 7 títulos distintos e possui um esquema de 
descontos que leva em consideração se é o mesmo título ou não. 
O problema consiste em calcular o melhor desconto para o cliente.

Preço de um título qualquer: R$ 42,00

Descontos:
    2 livros - 5%
    3 livros - 10%
    4 livros - 15%
    5 livros - 20%
"""

class Livraria:
    def __init__(self):
        self.items = [
            {"id": 1, "titulo": "Harry Potter e a Pedra Filosofal", "preco_unitario": 18.59},
            {"id": 2, "titulo": "Harry Potter e a Câmara Secreta", "preco_unitario": 15.29},
            {"id": 3, "titulo": "Harry Potter e o Prisioneiro de Azkaban", "preco_unitario": 16.39},
            {"id": 4, "titulo": "Harry Potter e o Cálice de Fogo", "preco_unitario": 19.59},
            {"id": 5, "titulo": "Harry Potter e a Ordem da Fênix", "preco_unitario": 20.29},
            {"id": 6, "titulo": "Harry Potter e o Enigma do Príncipe", "preco_unitario": 22.89},
            {"id": 7, "titulo": "Harry Potter e as Relíquias da Morte", "preco_unitario": 27.99},
        ]

        self.carrinho = []

    def get_item_by_id(self, id):
        item = next((item for item in self.items if item["id"] == id), None)
        
        if item == None:
            raise Exception("Livro não encontrado. ID incorreto")
            return {}
        else:
            return item

    # adiciona item ao carrinho
    def adicionar_item_carrinho(self, item):
        if item:
            self.carrinho.append(item)
        
        else:
            raise TypeError("Item não informado corretamente")

    # calcula valor total do carrinho, considerando descontos
    def calcular_valor_carrinho(self):
        valor_total = 0
        descontos = self.calcular_descontos_carrinho()
        for item in self.carrinho:
            valor_total += item['preco_unitario'] * item['quantidade'] - descontos[item['id']]

        return valor_total

    # calcula desconto de um único item do carrinho
    def calculcar_desconto_item(self, item):
        if self.get_item_by_id(item['id']):
            if item['quantidade'] == 2:
                percentual =  0.05
            elif item['quantidade'] == 3:
                percentual = 0.1 
            elif item['quantidade'] == 4:
                percentual = 0.15  
            else:
                percentual = 0.2  

            total = item['preco_unitario'] * item['quantidade']

            return total * percentual
        else:
            raise TypeError("Item não informado corretamente")

    # calcula desconto de todos os itens do carrinho, e coloca os descontos separados em um dicionario
    def calcular_descontos_carrinho(self):
        descontos = {}
        for item in self.carrinho:
            descontos[item['id']] = self.calculcar_desconto_item(item)
        
        return descontos

    # calcula melhor valor com desconto a partir de uma lista de itens
    def calcular_melhor_desconto(self, itens):
        menor_valor = 0
    
        for item in itens:
            # se valor ainda for zero, seta o menor valor como o do primeiro item
            if menor_valor == 0:
                menor_valor = item["preco_unitario"] * item['quantidade'] - self.calculcar_desconto_item(item)

            else:
                valor_com_desconto = item["preco_unitario"] * item['quantidade'] - self.calculcar_desconto_item(item)
                if valor_com_desconto < menor_valor:
                    menor_valor = valor_com_desconto

        return menor_valor

    def get_carrinho(self):
        return self.carrinho