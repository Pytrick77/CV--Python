palavras = 'amor', 'saudade', 'gentileza', 'prosperidade', 'fraterno', 'futebol', 'dinheiro'

for letra in palavras:
    print(f'\nNa palavra {letra.upper()} temos as vogais: ', end='')
    for vogal in letra:
        if vogal == 'a':
            print('a', end=' ')
        elif vogal == 'e':
            print('e', end=' ')
        elif vogal == 'i':
            print('i', end=' ')
        elif vogal == 'o':
            print('o', end=' ')
        elif vogal == 'u':
            print('u', end=' ')

# Outra forma de resolver usando somente um if:

        # if vogal in 'aeiou':
        #     print(vogal, end=' ')
