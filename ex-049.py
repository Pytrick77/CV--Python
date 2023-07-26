print(f'{"Vamos jogar tabuada?":^40}')
numero = int(input('Digite um número: '))

print(f'A tabuada de {numero} é:')
print("=*="*20)

for i in range (1, 11):
    print(f'{numero} x {i} = {numero*i}')

print("=*="*20)
