from datetime import date

sexo = int(input('''Sobre seu sexo informe: 
[ 1 ] - MASCULINO
[ 2 ] - FEMININO
[ 3 ] - NÃO DEFINIDO
Opção escolhida: '''))

if sexo == 1:

    ano = int(input('Informe seu ano de nascimento: '))
    hoje = date.today().year
    idade = hoje - ano
    print(f'Já que nasceu em {ano} tem {idade} anos em {hoje}.')

    if idade < 18:
        print('Você ainda vai se alistar ao serviço militar.')
        print('Faltam {} anos para você se alistar, no ano de {}!!'.format(18 - idade, ano + 18))

    elif idade == 18:
        print('Já é hora de se alistar ao serviço militar!')

    else:
        print('Já passou do tempo de alistamento.')
        print('Você deveria ter se alistado à {} anos, em {}!!'.format(idade - 18,hoje - (idade - 18)))

elif sexo == 2 or sexo == 3 :
    print('O serviço militar não é obrigatório para você.')
    print('Tenha um bom dia!!!')

else:
    print('''Digite uma opção válida!!
Tenha um bom dia!!!''')
