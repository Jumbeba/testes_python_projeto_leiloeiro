from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

rafa = Usuario('Rafa')
karol = Usuario('Karol')

lance_do_rafa = Lance(rafa, 100.0)
lance_da_karol = Lance(karol, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_da_karol)
leilao.lances.append(lance_do_rafa)

for lance in leilao.lances:
    print(f'Usuário {lance.usuario.nome}, deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance}, e o maior lance foi de {avaliador.maior_lance}')