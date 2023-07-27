# Exercício para descobrir se uma frase é ou não um palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()
frase_separada = frase.replace(' ', '')
frase_junta = ''

for i in range (len(frase_separada) - 1, -1, -1):
    frase_junta += frase_separada[i]


print(f'A frase {frase_separada} invertida fica {frase_junta}!')

if frase_separada == frase_junta:
    print('Temos um palíndromo.')

else:
    print('A frase não é um palíndromo.')