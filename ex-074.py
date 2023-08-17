import numpy as np

sorteio = tuple(np.random.randint(0, 11, 5))

maior = max(sorteio)
menor = min(sorteio)
print(f'Os valores sorteados foram:',end=' ')

for cont in range(0, len(sorteio)):
    print(sorteio[cont], end=' ')

print(f'\nO maior valor sorteado foi {maior}!')
print(f'O menor valor sorteado foi {menor}!')


# Outra forma de fazer o sorteio dos itens

# from random import randint

# sorteio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10),)
# print(sorteio)
