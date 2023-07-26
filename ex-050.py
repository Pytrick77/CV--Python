soma = 0
count = 0
for i in range (1, 7):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0:
        soma += n
        count += 1

print(f'A soma dos {count} números pares é de {soma}!')
