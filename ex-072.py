numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

n = int(input('Digite um número entre 0 e 20: '))

while n not in range(0, 21):
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    
print(f'Você digitou o número {numeros[n]}.')


# Outra forma de usar o While e fazendo o programa parar conforme a vontade do usúario.

# while True:
#     n = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= n <= 20:       
#         print(f'Você digitou o número {numeros[n]}.')
#         continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#         if continuar == 'N':
#             break
#     else:
#         print('Tente novamente.', end=' ')

# print('Você saiu do programa.')
