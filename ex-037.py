
numero = int(input('Digite qualquer número inteiro: '))
escolhas = input('''Escolha entre as opções abaixo:
[ 1 ]- Binário 
[ 2 ]- Octal 
[ 3 ]- Hexadecimal 
Sua escolha: ''')

if escolhas == "1":
    bi = bin(numero)
    print('O número {} em binário fica {}!'.format(numero,bi.replace('0b','')))
elif escolhas == "2":
    octa = oct(numero)
    print('O número {} em oct fica {}!'.format(numero,octa.replace('0o','')))
elif escolhas == "3":
    hexa = hex(numero)
    print('O número {} em hexadecimal fica {}!'.format(numero,hexa.replace('0x','')))
else:
    print('Opção inválida!!')