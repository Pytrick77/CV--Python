from random import randint
from time import sleep
print('Valores Sorteados: ')
sleep(2)
dados = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}
for k, v in dados.items():
    print(end=('      '))
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ordenados = sorted(dados.items(), key=lambda x: x[1], reverse=True)
print('=-' * 30)
print('Ranking dos Jogadores: ')
sleep(2)
for item, jogador in enumerate(ordenados):
    print(end=('      '))
    print(f'{item + 1}° Lugar: {jogador[0]} com {jogador[1]}.')
    sleep(1)

# Outra forma de ordenar o ranking usando a biblioteca itemgetter
# from operator import itemgetter
# ranking = list()
# ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
# print('Ranking dos Jogadores: ')
# sleep(2)
# for item, jogador in enumerate(ranking):
#     print(end='      ')
#     print(f'{item + 1}° Lugar: {jogador[0]} com {jogador[1]}.')
#     sleep(1)
