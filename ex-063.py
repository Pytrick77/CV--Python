print(f'{"Sequência de Fibonacci":^40}')

n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
count = 1
termo3 = 0

while count <= n:
    print(termo3, '> FIM' if count == n else '> ', end='')
    termo1 = termo2
    termo2 = termo3
    termo3 = termo1 + termo2
    count += 1
