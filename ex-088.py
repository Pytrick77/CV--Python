from random import randint
from time import sleep
print(f'{"Sorteador de Números para a Mega-Sena":^50}')
sorteio = []
jogos = []
sleep(2)
quant_jogos = int(input('Quantos jogos quer sortear? '))
jogos_sorteados = 1
while jogos_sorteados <= quant_jogos:
    count = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in sorteio:
            sorteio.append(numeros)
            count += 1
        if count == 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    jogos_sorteados += 1
sleep(2)
print('=+=' * 5, f' Sorteando {quant_jogos} Jogos: ', '=+=' * 5)
sleep(2)
for indice, jogo in enumerate(jogos):
    print(f'Jogo {indice+1}: {jogo}')
    sleep(1)
print('Obrigado por usar o Programa. Volte sempre!!!')
