from datetime import date

hoje = date.today().year
menor = 0
maior = 0

for i in range (1, 8):
    ano = int(input(f'Informe o ano de nascimento da {i}° pessoa: '))
    idade = hoje - ano
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1

print(f'{menor} pessoas são menores de idade e {maior} pessoas tem 21 anos ou mais!')
