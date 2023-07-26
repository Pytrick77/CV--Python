reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))

triangulo = reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2
equilatero = reta1 == reta2 == reta3
escaleno = reta1 != reta2 != reta3 != reta1

if triangulo:
    if escaleno:
        print('As retas formam um triângulo escaleno.')
    elif equilatero:
        print('As retas formam um triângulo equilátero.')
    else:
        print('As retas formam um triângulo isósceles.')
else:
    print('As retas não formam um triângulo.')


