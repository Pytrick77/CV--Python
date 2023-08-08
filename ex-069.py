mais_18 = menos_20 = homem = 0

while True:
    print(f'{"Cadastre uma pessoa":^40}')
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    print('-'*40)
    
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    print('-'*40)

    if idade > 18:
        mais_18 += 1

    if sexo == 'F' and idade < 20:
        menos_20 += 1

    if sexo == 'M':
        homem += 1

    if continuar == 'N':
        break

print(f'{"FIM DO PROGRAMA!":^40}')
print('-'*40)
print(f'Total de pessoas com mais de 18 anos: {mais_18}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {menos_20} mulheres com menos de 20 anos.')
