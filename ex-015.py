d = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de km percorridos: '))

custo_total = (d*60)+ (km*0.15)

print('O total a pagar é R${:.2f}'.format(custo_total))