def area(l, c):
    area_calcu = l * c
    print(f'A área de um terreno de {l}x{c} é de {area_calcu}m².')


print(f'Controle de Terrenos')
print('-' * 20)
area(l=float(input('LARGURA (m): ')), c=float(input('COMPRIMENTO (m): ')))
