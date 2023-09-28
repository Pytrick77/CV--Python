from datetime import date 
ano_atual = date.today().year 
dados = {
    'nome': str(input('Nome: ')).strip().title(),
    'idade': ano_atual - int(input('Ano de nascimento: ')),
    'cpts': int(input('Carteira de trabalho (0 não tem): '))}
if  dados['cpts'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Sálario: R$'))
    dados['aposetadoria'] = dados['idade'] + (dados['contratação'] + 35) - ano_atual  
print('-=-=' * 20)
for k, v in dados.items():
    print(f'  - {k} tem o valor de {v}')
