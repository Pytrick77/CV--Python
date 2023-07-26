n = int(input('Digite o primeiro termo: '))
razao = int(input('Digite sua razão: '))
pa = n

print(f'Os 10 primeiros termos da progressão aritmética do número {n} com razão {razao} são:')

for i in range (1 , 11):
    print(f'{i}° Termo: {pa}')
    pa += razao

print('Acabou!')

# Outra forma de resolver o exercício:


# for i in range (1, 11, pa):
#     print(f'{i}° Termo: {pa}')
#     pa += razao
