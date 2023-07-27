# Exercício de maior e menor pesos de uma sequencia de 6 entradas

maior = 0
menor = 0

for i in range(1,7):
    peso = float(input(f'Informe o peso da {i}° Pessoa: '))
    
    if peso > maior:
        maior = peso

    elif menor == 0 or menor > peso:
        menor = peso

print(f'O maior peso é de {maior:.1f}kg e o menor é de {menor:.1f}kg!')


# Outra forma de resolver o exercício com listas.

# lista = []

# for i in range (1,6):
#     peso = float(input(f'Informe o peso da {i}° pessoa: '))
#     lista += [peso]
#     # lista.append(peso) Outra forma de adicionar os pesos na lista
# maior = max(lista)
# menor = min(lista)
# print(maior, menor)
