from math import hypot

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

hypo = hypot(co , ca)

print('O cateto oposto {:.2f} + o cateto adjacente {:.2f}, retorna o valor do comprimento da hipotenusa de {:.2f}!'.format(co,ca,hypo))

# Forma de resolver o problema sem importar nada.

print('*'*50)
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

h = (co**2 + ca **2) ** (1/2)

print('A hipotenusa é igual a: {:.2f}!'.format(h))
print('*'*30)