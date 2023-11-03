c = ('\033[m',
        '\033[0;30;41m',
        '\33[0;30;44m',
        '\33[0;30;43m'
        );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo', 3)