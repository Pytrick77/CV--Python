numbers = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)
print('+=+=' * 24)
print(f'Os valores pares digitados foram {sorted(numbers[0])}')
print(f'Os valores ímpares digitados foram {sorted(numbers[1])}')
