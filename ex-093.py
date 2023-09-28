nome = str(input('Nome do Jogador: ')).strip().title()
dados = {
    'nome': nome,
    'gols': []}
quant_partidas = int(input(f'Quantas partidas {nome} jogou? '))
gols = []
for i in range(1, quant_partidas + 1):
    gols.append(int(input(f'   Quantos gols na partida {i}? ')))
print('-=-=' * 20)
dados['gols'] = gols
# total_gols = sum(gols) Outra forma de somar os gols
total_gols = 0
for gol in gols:
    total_gols += gol
dados['total'] = total_gols
print(dados)
print('-=-=' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-=' * 20)
print(f'O jogador {dados["nome"]} jogou {quant_partidas} partidas.')
for i, p in enumerate(dados['gols']):
    print(end='      => ')
    print(f'Na partida {i + 1}, fez {p} gols.')
print(f'Foi um total de {dados["total"]} gols.')
