numero = int(input('Informe um número: '))
count = 0

print(f'Os divisores de {numero} são:')

for i in range (1 , numero + 1):
    if numero % i == 0: 
       count += 1
       print(f'\033[31m{i}\033[m')

if count == 2:
    print(f'O número {numero} é \033[32mPRIMO\033[m, pois tem {count} divisores.')  
else:
    print(f'O número {numero} é \033[33mNÃO É PRIMO\033[m, pois tem {count} divisores.')   
