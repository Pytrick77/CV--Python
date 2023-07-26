casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
anos = int(input('Informe em quantos anos irá pagar: '))

meses = anos * 12
prestacao = casa / meses
porcentagem = ( prestacao * 100) / salario

if porcentagem > 30:
    print('Empréstimo não aprovado!!! A prestação de R${:.2f} mensais excede 30% do salário.'.format(prestacao))
    print('A porcentagem hoje é de {:.2f}%'.format(porcentagem))
else:
    print('Empréstimo aprovado!!. A prestação de {:.2f}R$ não excede 30% do salário.'.format(prestacao))
    print('A porcentagem hoje é de {:.2f}%'.format(porcentagem))
    print('A prestação mensal será de R${:.2f}! Para ser paga em {} meses!'.format(prestacao,meses))


