# Exercício para descobrir o homem mais velho, quantas mulheres tem menos de 20 anos e qual a média de idade do grupo. 4 entradas

nome_homem = ''
idade_homem = 0
mulher_menor = 0
soma = 0

for i in range (1,5):
    print(f"{10 * '-'} {i}° Pessoa {10 * '-'}")
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma+= idade

    if sexo == 'M' and idade > idade_homem:
        nome_homem = nome
        idade_homem = idade

    elif sexo == 'F' and idade < 20:
        mulher_menor += 1

media = soma / 4

print(f'A média de idade do grupo é de {media} anos.')

if mulher_menor == 0:
    print(f'No grupo não têm mulheres menores de 20 anos.')

elif mulher_menor > 1:
    print(f'No grupo têm {mulher_menor} mulheres menores de 20 anos.')

else:
    print(f'No grupo tem {mulher_menor} mulher menor de 20 anos.')

print(f'O homem mais velho do grupo se chama {nome_homem} e ele tem {idade_homem} anos.')
