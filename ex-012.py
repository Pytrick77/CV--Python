p = float(input('Informe o preço do produto: R$'))
novo_preco = p - ((p * 5) / 100) 

print('O preço do produto com desconto de 5% é igual é: R$ {:.2f}!'.format(novo_preco))