l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = a * l
tinta = 2
quant = area / 2

print('A quantidade de tinta necessária para pintar uma área de {:.1f}, é de {:.1f}l de tinta'.format(area,quant))