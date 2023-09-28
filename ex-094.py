dados = {}
geral = []
total = media = 0
maior_media = []
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]   
    if dados['sexo'] not in 'MmFf':
        print('Erro!!! Por favor digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    geral.append(dados.copy())
    total += dados['idade']
    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar not in 'SsNn':
        print('Erro!!! Responda apenas S ou N.')
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if dados['idade'] > media:
        maior_media.append([dados['nome'], dados['sexo'], dados['idade']])
    if continuar in 'N':
        break
media = total / len(geral)
print('=-=-' * 20)
print(f'A) O grupo tem {len(geral)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for mulher in geral:
    if mulher['sexo'] in 'F':
        print(f'{mulher["nome"]}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for i in maior_media:
    if i[2] > media:
        print(f'    Nome = {i[0]}; sexo = {i[1]}; idade = {i[2]};')       
print('==>>> Encerrado <<<==')
