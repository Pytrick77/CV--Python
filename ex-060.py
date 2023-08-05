numero = int(input('Digite um número para calcular seu Fatorial: '))

fatorial = 1

print(f'Calculando {numero}! =', end=' ')

while numero != 0:
    print(f'{numero}', end= ' ')
    # print('x ' if numero > 1 else '= ', end='') Outra forma de colocar o 'x' ou '='.
    fatorial *= numero
    numero -= 1
    if numero != 0:
        print('x', end=' ')

print(f'= {fatorial}')


#  Resolução usando laço For:

# if numero > 0:
#     for i in range(1, numero):
#         fatorial *= numero
#         numero -= 1

# print(f'{fatorial}')
