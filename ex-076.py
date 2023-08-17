print('-'*30)
print(f'{"Listagem de Preços":^30}')
print('-'*30)

listagem = 'Arroz', 10.50, 'Macarrão', 3.50, 'Feijão', 8.30, 'Camiseta', 50.00, 'Shorts', 35.70

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<15}', end='')
    else:
        print(f'{listagem[i]:>10.2f}')
