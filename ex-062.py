print(f"{'Gerador de PA':^40}" )

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
quantidade = int(input('Quantos termos quer mostrar? '))
quant_termos = 0
i = 1

while quantidade != 0:
    while i <= quantidade:
        print(primeiro, end=' > ')
        primeiro += razao
        quant_termos += 1
        i += 1
    print('Pausa')

    quantidade = int(input('Quantos termos quer a mais? '))
    i = 1

print(f'Ao todo foram exibidos {quant_termos} termos.')
