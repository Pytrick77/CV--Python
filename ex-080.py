lista = []

for i in range(5):
    numero = int(input('Digite um número: '))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print('-=-' * 20)
print(lista)

# Resolução do exercício usando o insort:

# from bisect import insort
# numeros = []

# for i in range(5):
#     numero = int(input('Digite um número: '))
#     insort(numeros, numero)
# print(f'A lista ordenada fica {numeros}.')