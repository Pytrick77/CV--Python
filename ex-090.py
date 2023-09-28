dados = {}
dados['nome'] = str(input('Nome: ')).strip().title()
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
print('=-=-' * 10)
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'
for k, v in dados.items():
    print(f' - {k} é igual a {v}')
