from moeda import * 

numero = float(input('Informe o preço: R$'))
print(f'Aumentando 10% temos R$ {aumentar(numero, 10)}')
print(f'Diminuindo 13% temos R$ {dmimnuir(numero, 13)}')
print(f'O dobro de R$ {numero} é igual a R$ {dobro(numero)}')
print(f'A metade de R$ {numero} é igual a R$ {metade(numero)}')
