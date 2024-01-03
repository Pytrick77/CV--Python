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

def leiaFloat(n):
    while True:
        try:
            numero = float(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!!! Por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero
