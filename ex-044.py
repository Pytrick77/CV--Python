print('{:-^50}'.format(' Lojas Patrick '))

preco = float(input('Informe o preço das compras: R$'))
condicao = int(input('''Informe a condição de pagamento: 
[ 1 ] - À vista dinheiro / cheque 
[ 2 ] - À vista no cartão 
[ 3 ] - 2x no cartão 
[ 4 ] - 3x ou mais no cartão
Qual opção?  '''))

if condicao == 1:
    total = preco - (preco * 10 / 100)   
elif condicao == 2:
    total = preco - (preco * 5 / 100)   
elif condicao == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!')
elif condicao == 4:
    total = preco + (preco * 20 / 100)
    vezes = int(input('Quantas parcelas? '))
    parcela = total / vezes
    print(f'Sua compra será parcelada em {vezes}x de R${parcela:.2f} com JUROS.')
else:
   total = preco
   print('Opção Inválida de pagamento. Tente novamente!!') 
print(f'O preço da compra de R${preco:.2f} vai custar R${total:.2f} no final!!')

