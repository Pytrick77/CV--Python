from random import choice
from time import sleep

cores = {"vermelho": "\033[31m" , "azul": "\033[34m", "fechamento": "\033[m" , "verde":"\033[32m" , "amarelo": "\033[033m", "roxo": "\033[35m" , "azulc": "\033[36m"}

print(f'{cores["azul"]}{"Está pronto para um desafio contra o computador??":^100}{cores["fechamento"]}')
sleep(3)

print(f'{cores["verde"]}Vamos jogar Pedra, Papel, Tesoura. Que vença o melhor, no caso eu. Ha ha ha ha!!!!{cores["fechamento"]}')
sleep(4)

usuario = str(input(f'{cores["roxo"]}Digite sua escolha: Tesoura, Papel, Pedra: {cores["fechamento"]}')).strip().title()
opcoes = ['Pedra', 'Papel', 'Tesoura']
print(f'{cores["amarelo"]}Vou fazer minha escolha...{cores["fechamento"]}')
sleep(4)

computador = choice(opcoes)
print(f'{cores["vermelho"]}{computador}{cores["fechamento"]}')

sleep(2)
if usuario == 'Pedra' and computador =='Tesoura':
    print('Parabéns, você venceu!')

elif computador == 'Pedra' and usuario =='Tesoura':
    print('Eu venci kkkkkk loser!!!')

elif usuario == 'Papel' and computador == 'Pedra' :
    print('Parabéns, você venceu!')

elif computador == 'Papel' and usuario == 'Pedra' :
    print('Eu venci kkkkkk loser!!!')

elif usuario == 'Tesoura' and computador == 'Papel':
    print('Parabéns, você venceu!')

elif computador == 'Tesoura' and usuario == 'Papel':
    print('Eu venci kkkkkk loser!!!')

else:
    print(f'{cores["azulc"]}Nossa escolha foi a mesma, empate. Vamos de novo?{cores["fechamento"]}')




