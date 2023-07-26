n = input('Digite um número entre 0 e 9999: ')

unidade = n[-1:]
dezena = n[-2:-1]
centena = n[-3:-2]
milhar = n[:-3]

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade,dezena,centena,milhar))

