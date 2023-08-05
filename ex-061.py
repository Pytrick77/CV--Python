print(f"{'Gerador de PA':^40}" )

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
i = 1

while i <= 10:
    print(primeiro, end=' > ')
    primeiro += razao
    i += 1
print('FIM')
