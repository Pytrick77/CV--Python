nome = str(input('Digite seu nome completo: ')).strip().title()

p = nome.split()

print('Seu primeiro nome é {}.\nE seu último nome é {}!'.format(p[0],p[-1]))