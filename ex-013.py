salario = float(input('Informe seu salário atual: R$'))
novo_s = salario + ((salario * 15)/100)

print('Com o novo aumento de 15% seu antigo salário que era de R${:.2f}, passa a ser agora R${:.2f}. Parabéns!!'.format(salario,novo_s))