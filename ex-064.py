numero = int(input('Digite um número [999 para parar]: '))
soma = contagem = 0

while numero != 999:
    if numero != 999:
        soma += numero
        contagem += 1
        numero = int(input('Digite um número  [999 para parar]: '))

print(f'Você digitou {contagem} números e a soma entre eles foi de {soma}.')
