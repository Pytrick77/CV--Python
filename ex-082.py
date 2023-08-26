numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'A lista completa do valores digitados é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
