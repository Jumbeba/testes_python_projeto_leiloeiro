from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


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

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # teste de validação de igualdade
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance_da_karol)
        self.leilao.propoe(self.lance_do_rafa)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leila_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_rafa)

        self.assertEqual(100.0, self.leilao.maior_lance)
        self.assertEqual(100.0, self.leilao.menor_lance)

    def test_deve_retornar_maior_e_menor_valor_quando_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini')

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(self.lance_da_karol)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        # teste de validação de igualdade
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_rafa)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    # se o último usuário for diferente, deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        vini = Usuario('Vini')
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(lance_do_vini)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o último usuário for o mesmo, não deve permitir propor lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_rafa200 = Lance(self.rafa, 200.0)

        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(lance_do_rafa200)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebido)

