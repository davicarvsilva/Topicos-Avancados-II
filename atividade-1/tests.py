import unittest

from Livraria import Livraria

class TestLivraria(unittest.TestCase):
    def setUp(self):
        self.livraria = Livraria()

    def test_get_item_by_id(self):
        item = self.livraria.get_item_by_id(7)
        self.assertIsInstance(item, dict)
        self.assertNotEqual(item, {})

    def test_adicionar_item_carrinho(self):
        item = self.livraria.get_item_by_id(7)
        item['quantidade'] = 2
        self.livraria.adicionar_item_carrinho(item)
        self.assertIn(item, self.livraria.carrinho)

    def test_calcular_desconto_item(self):
        item1 = self.livraria.get_item_by_id(1)
        item2 = self.livraria.get_item_by_id(2)
        item3 = self.livraria.get_item_by_id(3)
        item4 = self.livraria.get_item_by_id(4)

        item1['quantidade'] = 2
        item2['quantidade'] = 3
        item3['quantidade'] = 4
        item4['quantidade'] = 5

        desconto_item1 = item1['quantidade'] * item1['preco_unitario'] * 0.05
        desconto_item2 = item2['quantidade'] * item2['preco_unitario'] * 0.1
        desconto_item3 = item3['quantidade'] * item3['preco_unitario'] * 0.15
        desconto_item4 = item4['quantidade'] * item4['preco_unitario'] * 0.20
        
        self.assertEqual(desconto_item1, self.livraria.calculcar_desconto_item(item1))
        self.assertEqual(desconto_item2, self.livraria.calculcar_desconto_item(item2))
        self.assertEqual(desconto_item3, self.livraria.calculcar_desconto_item(item3))
        self.assertEqual(desconto_item4, self.livraria.calculcar_desconto_item(item4))

    def test_calcular_valor_carrinho(self):
        item1 = self.livraria.get_item_by_id(1)
        item2 = self.livraria.get_item_by_id(2)

        item1['quantidade'] = 2
        item2['quantidade'] = 3

        self.livraria.adicionar_item_carrinho(item1)
        self.livraria.adicionar_item_carrinho(item2)

        desconto_item1 = self.livraria.calculcar_desconto_item(item1)
        desconto_item2 = self.livraria.calculcar_desconto_item(item2)

        desconto_total = desconto_item1 + desconto_item2

        valor_carrinho = self.livraria.calcular_valor_carrinho()

        self.assertEqual(valor_carrinho, (item1['preco_unitario'] * item1['quantidade']) + 
            (item2['preco_unitario'] * item2['quantidade']) - desconto_total)

    def test_calcular_descontos_carrinho(self):
        item1 = self.livraria.get_item_by_id(1)
        item2 = self.livraria.get_item_by_id(2)

        item1['quantidade'] = 2
        item2['quantidade'] = 3

        self.livraria.adicionar_item_carrinho(item1)
        self.livraria.adicionar_item_carrinho(item2)

        desconto_item1 = self.livraria.calculcar_desconto_item(item1)
        desconto_item2 = self.livraria.calculcar_desconto_item(item2)

        descontos = self.livraria.calcular_descontos_carrinho()

        self.assertEqual(desconto_item1, descontos[item1['id']])
        self.assertEqual(desconto_item2, descontos[item2['id']])

    def test_calcular_melhor_desconto(self):
        item1 = self.livraria.get_item_by_id(1)
        item2 = self.livraria.get_item_by_id(2)
        item3 = self.livraria.get_item_by_id(3)

        item1['quantidade'] = 2
        item2['quantidade'] = 5
        item3['quantidade'] = 3

        itens = [item1, item2, item3]

        self.livraria.adicionar_item_carrinho(item1)
        self.livraria.adicionar_item_carrinho(item2)
        self.livraria.adicionar_item_carrinho(item3)

        valores_itens_com_desconto = []

        for item in itens:
            valor = {}
            valor['id'] = item['id']
            valor['valor'] = (item['quantidade'] * item['preco_unitario'] - 
                self.livraria.calculcar_desconto_item(item))

            valores_itens_com_desconto.append(valor)

        melhor_valor_com_desconto = self.livraria.calcular_melhor_desconto(itens)

        self.assertEqual(min(valores_itens_com_desconto, key=lambda x: x['valor'])['valor'],
            melhor_valor_com_desconto)

if __name__ == '__main__':
    unittest.main()
