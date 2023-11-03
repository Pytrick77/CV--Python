def ficha(jogad='<desconhecido>', gols=0):
    print(f'O jogador {jogad} fez {gols} gol(s) no campeonato.')


print('-' * 25)
jogador = input('Nome do jogador: ').strip().title()
quant_gols = input('Número de gols: ')
if quant_gols.isnumeric():
    quant_gols = int(quant_gols)
else:
    quant_gols = 0
if not jogador:
    ficha(gols = quant_gols)
else:
    ficha(jogador, quant_gols)