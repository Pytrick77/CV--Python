while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    count = 1
    print('-'*30)

    if numero <= 0:
        break

    while count <= 10:   
        tabuada = numero * count
        count += 1
        print(f'{numero} x {count} = {tabuada}')
    print('-'*30)

print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

# Resolução usando o for: 

    # for i in range (1, 11):
    #     tabuada = numero * i
    #     print(f'{numero} x {i} = {tabuada}')
