from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        self.rafa = Usuario('Rafa')
        self.karol = Usuario('Karol')
        self.lance_do_rafa = Lance(self.rafa, 100.0)
        self.lance_da_karol = Lance(self.karol, 150.0)
        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(self.lance_da_karol)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # teste de validação de igualdade
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_da_karol)
        self.leilao.propoe(self.lance_do_rafa)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leila_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_rafa)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(100.0, avaliador.maior_lance)

    def test_deve_retornar_maior_e_menor_valor_quando_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini')

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(self.lance_da_karol)
        self.leilao.propoe(lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        # teste de validação de igualdade
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
