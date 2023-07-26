from math import trunc

num = float(input('Digite um número de ponto flutuante: '))
nint = trunc(num)

print('O número {} tem a parte inteira {}!'.format(num,nint))

# Outra forma de resolver o mesmo exercício sem importar nenhum módulo.

print('-'*20)
n = float(input('Informe um número: '))

print('O número digitado foi {} e sua parte inteira é {}.'.format(n,int(n)))

print('-'*20)
