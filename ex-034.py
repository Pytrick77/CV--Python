salario = float(input('Informe seu salário: '))

if salario <= 1250:
    aumento = salario + (salario * 15 /100)
    print('Seu novo salário com reajuste de 15% é igual à {:.2f}'.format(aumento))
else:
    aumen = salario + (salario * 10 / 100)
    print('Seu novo salário com reajuste de 10% é igual à {:.2f}'.format(aumen))