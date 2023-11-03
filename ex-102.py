def fatorial(num=1, show=False):
    '''
    -> Calcula o Fatorial de um número;
    :param num: O número a ser calculado;
    :param show: (Opcional) Mostrar ou não a conta;
    :return: O valor do Fatorial de um número n.
    '''
    cont = 1
    while num > 0:
        if show:
            print(num, end=' ')
            if num > 1:
                print('x', end=' ')
            if num == 1:
                print('=', end=' ')
        cont *= num
        num -= 1  
    return cont


print('-' * 30)
print(fatorial(5, True))
