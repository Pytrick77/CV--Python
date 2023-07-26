from random import randint

palpite = int(input('Tente adivinhar o número entre 0 e 5: '))
n = randint(0,5)

if palpite == n:
    print('Parabéns o chute foi correto!!!')
else:
    print('Infelizmente você errou!')

print('O número gerado foi {}.'.format(n))
