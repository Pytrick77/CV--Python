matriz = [[], [], []]
pares = maior = 0
matriz[0].append(int(input('Digite o valor da posição [0, 0]: ')))
matriz[0].insert(1, int(input('Digite o valor da posição [0, 1]: ')))
matriz[0].insert(2, int(input('Digite o valor da posição [0, 2]: ')))
matriz[1].append(int(input('Digite o valor da posição [1, 0]: ')))
matriz[1].insert(1, int(input('Digite o valor da posição [1, 1]: ')))
matriz[1].insert(2, int(input('Digite o valor da posição [1, 2]: ')))
matriz[2].append(int(input('Digite o valor da posição [2, 0]: ')))
matriz[2].insert(1, int(input('Digite o valor da posição [2, 1]: ')))
matriz[2].insert(2, int(input('Digite o valor da posição [2, 2]: ')))
for item in matriz:
    for i in item:
        if i % 2 == 0:
            pares += i
soma_terceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maior = matriz[1][0]
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    maior = matriz[1][1]
else:
    maior = matriz[1][2]
print('=-=' * 20)
for i in matriz:
    print(' '.join([f'[ {num:^5} ]' for num in i]))
print('=-=' * 20)

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira}.')
print(f'O maior valor da segunda linha é {maior}.')

# # Outra forma de resolver o exercício:

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# soma_par = maior = terceira_coluna = 0 
# for linha in range(3):
#     for coluna in range(3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]:'))
# print('+=+=' * 23)
# for linha in range(3):
#     for coluna in range(3):
#         print(f'[{matriz[linha][coluna]:^5}]', end='')
#         if matriz[linha][coluna] % 2 == 0:
#             soma_par += matriz[linha][coluna]
#     print()
# print('+=+=' * 23)
# print(f'A soma dos valores pares é {soma_par}.')
# for linha in range(3):
#     terceira_coluna += matriz[linha][2]
# print(f'A soma dos valores da terceira coluna é {terceira_coluna}.')
# for coluna in range(3):
#     if coluna == 0:
#         maior = matriz[1][coluna]
#     elif matriz[1][coluna] > maior:
#         maior = matriz[1][coluna]
# print(f'O maior valor da segunda coluna é de {maior}.')
