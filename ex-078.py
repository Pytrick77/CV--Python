valores = []
maior = []
menor = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))

for pos, valor in enumerate(valores):
    if valor == max(valores):
        maior.append(pos)
    if valor == min(valores):
        menor.append(pos)

print('*+*' * 20)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {max(valores)} nas posições {maior}.')
print(f'O menor valor digitado foi {min(valores)} nas posições {menor}.')
