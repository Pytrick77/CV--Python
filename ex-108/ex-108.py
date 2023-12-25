from moeda import * 

numero = float(input('Informe o preço: R$'))
print(f'Aumentando 10% temos {moedas(aumentar(numero, 10))}')
print(f'Diminuindo 13% temos {moedas(dmimnuir(numero, 13))}')
print(f'O dobro de {moedas(numero)} é igual a {moedas(dobro(numero))}')
print(f'A metade de R$ {moedas(numero)} é igual a {moedas(metade(numero))}')
