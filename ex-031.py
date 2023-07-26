distancia = float(input('Informe a distância da sua viagem: '))

if distancia >= 200:
    valor = distancia * 0.45
    print('O valor da passagem será {:.2f} reais'.format(valor))
else:
    maior = distancia * 0.50
    print('O valor da passagem sera {:.2f} reais'.format(maior))

print('Boa viagem!!')