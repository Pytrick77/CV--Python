soma = 0
count = 0

for i in range (1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        count += 1
        
print(f'A soma de todos os \033[31m{count}\033[m valores ímpares e múltiplos de 3 em um intervalo de 1 a 500 é de \033[32m{soma}\033[m!')
