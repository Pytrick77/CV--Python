todos_jogadores = []
total = 0
while True:
    print('-' * 26)
    nome = str(input('Nome do Jogador: ')).strip().title()
    dados = {
        'nome': nome,
        'gols': []}
    quant_partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols = []
    for i in range(quant_partidas):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    dados['gols'] = gols
    total_gols = 0
    for gol in gols:
        total_gols += gol
    dados['total'] = total_gols
    todos_jogadores.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0] 
        if continuar in 'SN':
            break
        print('Erro!! Responda apenas S ou N.')    
    if continuar == 'N':
        break
print('-=-=' * 25)
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 56)
for k, v in enumerate(todos_jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 56)
while True:
    resposta = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resposta == 999:
        break
    if resposta >= len(todos_jogadores):
        print(f'ERRO!!! Não existe jogador com o código {resposta}! Tente novamente.')
        print('-' * 56)
    else:
        print(f'==> LEVANTAMENTO DO JOGADOR {todos_jogadores[resposta]["nome"]}:')
        for i, p in enumerate(todos_jogadores[resposta]['gols']):
            print(f'   --> No jogo {i}, fez {p} gols.')
        print('-' * 56)
print('VOLTE SEMPRE!!!')
