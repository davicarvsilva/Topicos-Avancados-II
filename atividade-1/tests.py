import unittest

from Livraria import Livraria

class TestLivraria(unittest.TestCase):
    def test_get_item_by_id(self):
        livraria = Livraria()
        item = livraria.get_item_by_id(7)
        
        self.assertIsInstance(item, dict) # verificar se o item recebido é mesmo um dicionário
        self.assertNotEqual(item, {}) # verifica se o item recebido não está vazio

    # verificar se item adicionado ao carrinho realmente consta no carrinho
    def test_adicionar_item_carrinho(self):
        livraria = Livraria()
        item = livraria.get_item_by_id(7)
        item['quantidade'] = 2 # define a quantida de livros a ser comprada
        livraria.adicionar_item_carrinho(item)
        expected_item = livraria.get_item_by_id(7)
        self.assertIn(expected_item, livraria.carrinho) 

    # verifica se o desconto calculado para um item bate com sua respectiva porcentagem
    # a depender da quantidade de livros 
    def test_calcular_desconto_item(self):
        livraria = Livraria()

        item1 = livraria.get_item_by_id(1)
        item2 = livraria.get_item_by_id(2)
        item3 = livraria.get_item_by_id(3)
        item4 = livraria.get_item_by_id(4)

        item1['quantidade'] = 2
        item2['quantidade'] = 3
        item3['quantidade'] = 4
        item4['quantidade'] = 5

        desconto_item1 = item1['quantidade'] * item1['preco_unitario'] * 0.05
        desconto_item2 = item2['quantidade'] * item2['preco_unitario'] * 0.1
        desconto_item3 = item3['quantidade'] * item3['preco_unitario'] * 0.15
        desconto_item4 = item4['quantidade'] * item4['preco_unitario'] * 0.20
        
        self.assertEqual(desconto_item1, 
            livraria.calculcar_desconto_item(item1))

        self.assertEqual(desconto_item2, 
            livraria.calculcar_desconto_item(item2))

        self.assertEqual(desconto_item3, 
            livraria.calculcar_desconto_item(item3))

        self.assertEqual(desconto_item4, 
            livraria.calculcar_desconto_item(item4))

    # verifica se o valor total do carrinho correspondo ao valor total dos itens
    def test_calcular_valor_carrinho(self):
        livraria = Livraria()
        item1 = livraria.get_item_by_id(1)
        item2 = livraria.get_item_by_id(2)

        item1['quantidade'] = 2
        item2['quantidade'] = 3

        livraria.adicionar_item_carrinho(item1)
        livraria.adicionar_item_carrinho(item2)

        desconto_item1 = livraria.calculcar_desconto_item(item1)
        desconto_item2 = livraria.calculcar_desconto_item(item2)

        desconto_total = desconto_item1 + desconto_item2

        valor_carrinho = livraria.calcular_valor_carrinho()

        self.assertEqual(valor_carrinho, 
            (item1['preco_unitario'] * item1['quantidade']) + 
            (item2['preco_unitario'] * item2['quantidade']) - 
            desconto_total)

    def test_calcular_descontos_carrinho(self):
        livraria = Livraria()
        item1 = livraria.get_item_by_id(1)
        item2 = livraria.get_item_by_id(2)

        item1['quantidade'] = 2
        item2['quantidade'] = 3

        livraria.adicionar_item_carrinho(item1)
        livraria.adicionar_item_carrinho(item2)

        desconto_item1 = livraria.calculcar_desconto_item(item1)
        desconto_item2 = livraria.calculcar_desconto_item(item2)

        descontos = livraria.calcular_descontos_carrinho()

        self.assertEqual(desconto_item1, descontos[item1['id']])
        self.assertEqual(desconto_item2, descontos[item2['id']])

    def test_calcular_melhor_desconto(self):
        livraria = Livraria()
        item1 = livraria.get_item_by_id(1)
        item2 = livraria.get_item_by_id(2)
        item3 = livraria.get_item_by_id(3)

        item1['quantidade'] = 2
        item2['quantidade'] = 5
        item3['quantidade'] = 3

        itens = [item1, item2, item3]

        livraria.adicionar_item_carrinho(item1)
        livraria.adicionar_item_carrinho(item2)
        livraria.adicionar_item_carrinho(item3)

        valores_itens_com_desconto = []

        # pega o subtotal (preco + desconto) dos itens setados anteriormente
        for item in itens:
            valor = {}
            valor['id'] = item['id']
            valor['valor'] = (item['quantidade'] * item['preco_unitario'] - 
                livraria.calculcar_desconto_item(item))

            valores_itens_com_desconto.append(valor)

        # pega o melhor desconto da lista de itens setada anteriormente
        melhor_valor_com_desconto = livraria.calcular_melhor_desconto(itens)

        # verifica se o menor desconto retornado da função calcular_melhor_desconto
        # é igual ao menor desconto da lista valores_itens_com_desconto (através da lamba function)
        self.assertEqual(min(valores_itens_com_desconto, key=lambda x: x['valor'])['valor'],
            melhor_valor_com_desconto)

if __name__ == '__main__':
    unittest.main()