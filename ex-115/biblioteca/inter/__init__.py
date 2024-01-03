def leiaInt(n):
    while True:
        try:
            numero = int(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!!! Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


def linha (tam=42):
    return '-' * tam


def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu (lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[35m{item}\033[m')
        contador += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
