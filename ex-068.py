from random import randint

print('=*='*15)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^40}')
print('=*='*15)

vitoria = 0

while True:
    valor_jogador = int(input('Digite um número: '))
    jogador = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 100)
    soma = valor_jogador + computador
    par_impar = jogador
    
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]

    if soma % 2 == 0:
        print(f'Você jogou {valor_jogador} e o computador {computador}. Total de {soma} deu Par. ')
        print('-'*45)
        
        if jogador == 'P':
            print('Você venceu. Vamos jogar novamente!')
            print('-'*45)
            vitoria += 1
        else:
            print('Você perdeu.')
            break
    else:
        print(f'Você jogou {valor_jogador} e o computador {computador}. Total de {soma} deu Ímpar. ')
        print('-'*45)

        if jogador == 'I':
            print('Você venceu. Vamos jogar novamente!')
            print('-'*45)
            vitoria += 1
        else:
            print('Você perdeu.')
            break

print('=*='*30)        
print(f'Game over. Você venceu {vitoria} vezes.')
