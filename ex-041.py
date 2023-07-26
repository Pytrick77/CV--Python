from datetime import date

ano = int(input('Informe seu ano de nascimento: ')) 
hoje = date.today().year
idade = hoje - ano

print(f'O atleta tem {idade}!')

if idade <= 9:
    print('Sua categoria é: Mirim')
elif idade <= 14:
    print('Sua categoria é: Infantil')
elif idade <= 19:
    print('Sua categoria é: Junior')
elif idade <= 25:
    print('Sua categoria é: Sênior')
else:
    print('Sua categoria é: Master')
