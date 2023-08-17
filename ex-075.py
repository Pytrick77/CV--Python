n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

cont_nove = 0
pares_lista = []
numeros = (n1, n2, n3, n4)

print(f'Você digitou os valores {numeros}.')

for numero in numeros:
    if numero == 9:
        cont_nove += 1
    elif numero % 2 == 0:
        pares_lista.append(numero)
        
print(f'O número 9 apareceu {cont_nove} vezes.')

if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição.')
else:
    print(f'O número 3 não apareceu.')

pares = tuple(pares_lista)

print(f'Os valores pares digitados foram ', end='')

for par in pares:
    print(par, end=' ')

# Outra forma de resolver o exercício:

# n = (int(input('Informe um número: ')), int(input('Informe um número: ')),
#      int(input('Informe um número: ')), int(input('Informe um número: ')))

# print(f'Os números digitados foram: {n}.')
# print(f'O número 9 apareceu {n.count(9)} vezes.')
# if 3 in n:
#     print(f'O número 3 apareceu na {n.index(3)+1}ª posição.')
# else:
#     print('O número 3 não foi digitado em nenhuma posição.')
# print(f'Os valores pares digitados foram ', end='')
# for numero in n:
#     if numero % 2 == 0:
#         print(numero, end=' ')
