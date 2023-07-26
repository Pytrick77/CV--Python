km = float(input('Informe a velociade do carro: '))

if km > 80:
    multa = (km - 80) * 7
    print('Você foi multado por estar acima do limite de velocidade permitido! \nSua multa foi de {:.2f} reais.'.format(multa))
else:
    print('Parabéns por dirigir na velocidade permitida!!')