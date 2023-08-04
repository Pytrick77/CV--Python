from random import randint  
from time import sleep

computador = randint(0, 10)

print('Oi, sou o seu computador...')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10...')
sleep(3)
print('Será que você consegue adivinhar qual foi? ')
sleep(2)

usuario = int(input('Qual é seu palpite? '))
sleep(2)
acertou = False
tentativa = 1

while not acertou:

    if usuario < computador:
        usuario = int(input('Mais... Tente mais uma vez. '))
        sleep(2)
    elif usuario > computador:
         usuario = int(input('Menos... Tente mais uma vez. '))
         sleep(2)
    elif usuario == computador:
        print(f'Parabéns você acertou, foram necessárias {tentativa} tentativas.')
        acertou = True
    tentativa += 1
