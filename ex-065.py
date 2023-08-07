numero = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
cont = 1
lista_numeros = [numero]
soma = numero

while continuar != 'N':
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    lista_numeros.append(numero)
    cont += 1
    soma += numero

media = soma / cont
maior = max(lista_numeros)
menor = min(lista_numeros)

print(f'Você digitou {cont} números e a média foi de {media:.2f}!')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
