valor = int(input('Qual valor quer sacar? R$'))
total = valor
cedula = 50
quant_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        quant_cedula += 1
    else:
        if quant_cedula > 0:
            print(f'Total de {quant_cedula} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        quant_cedula = 0
        if total == 0:
            break
