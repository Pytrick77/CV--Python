from moeda import * 

numero = float(input('Informe o preço: R$'))
print(f'Aumentando 10% temos {aumentar(numero, 10)}')
print(f'Diminuindo 13% temos {dmimnuir(numero, 13,True)}')
print(f'O dobro de {moedas(numero)} é igual a {dobro(numero,True)}')
print(f'A metade de R$ {moedas(numero)} é igual a {metade(numero)}')
