n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

if n1 > n2:
    print('O {} é maior que o {}!'.format(n1,n2))
elif n2 > n1:
    print('O {} é maior que o {}!'.format(n2,n1))
else:
    print('Não existe valor maior, os dois são iguais!!!')
