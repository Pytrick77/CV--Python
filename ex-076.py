print('-'*30)
print(f'{"Listagem de Preços":^30}')
print('-'*30)

listagem = 'Arroz', 10.50, 'Feijão', 8.00, 'Óleo', 7.98, 'Sal', 4.85, 'Açúcar', 7.49

for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f'{listagem[itens]:.<20}', end='')
    else:
        print(f'R${listagem[itens]:>7.2f}')