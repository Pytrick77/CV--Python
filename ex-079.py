numeros = []

while True:
    numero = int(input('Digite um valor: '))

    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso.')

    else:
        print('Valor duplicado. O mesmo não será adicionado.')

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]


    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

numeros.sort()

print('*=*' * 20)
print(f'Você digitou os valores {numeros}.')
