matriz = [[], [], []]
matriz[0].append(int(input('Digite o valor da posição [0, 0]: ')))
matriz[0].insert(1, int(input('Digite o valor da posição [0, 1]: ')))
matriz[0].insert(2, int(input('Digite o valor da posição [0, 2]: ')))
matriz[1].append(int(input('Digite o valor da posição [1, 0]: ')))
matriz[1].insert(1, int(input('Digite o valor da posição [1, 1]: ')))
matriz[1].insert(2, int(input('Digite o valor da posição [1, 2]: ')))
matriz[2].append(int(input('Digite o valor da posição [2, 0]: ')))
matriz[2].insert(1, int(input('Digite o valor da posição [2, 1]: ')))
matriz[2].insert(2, int(input('Digite o valor da posição [2, 2]: ')))
print('=-=' * 20)
for i in matriz:
    print(' '.join([f'[ {num:^5} ]' for num in i]))

# Outra forma de resolver o exercício:

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for linha in range(3):
#     for coluna in range(3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]:'))
# print('+=+=' * 23)
# for linha in range(3):
#     for coluna in range(3):
#         print(f'[{matriz[linha][coluna]:^5}]', end='')
#     print()
