total_compra = mais_mil = mais_barato = 0
nome_do_mais_barato = ''

print(f'{"Lojas Patrick":^50}')

while True:
    nome = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    total_compra += preco
    continuar = ' '

    if preco < mais_barato or mais_barato == 0:
        mais_barato = preco
        nome_do_mais_barato = nome

    if preco > 1000:
        mais_mil += 1

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'{"FIM DO PROGRAMA":-^50}')
print(f'O total da compra foi de R${total_compra:.2f}!')
print(f'Temos {mais_mil} produtos custando mais de R$1000.00!')
print(f'O produto mais barato foi {nome_do_mais_barato} que custa R${mais_barato:.2f}.')
