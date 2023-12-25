def aumentar(n=0, porcen=0, format=False):
    aumento = n + (n * (porcen / 100))
    if format:
        aumento = f'R${aumento:.2f}'.replace('.', ',')
    return aumento


def dmimnuir(n=0, porcen=0, format=False):
    menos = n - (n * (porcen / 100))
    if format:
        menos = f'R${menos:.2f}'.replace('.', ',')
    return menos


def dobro(n=0, format=False):
    dobrar = n * 2
    return dobrar if format is False else moedas(dobrar)


def metade(n=0, format=False):
    meio = n / 2
    return meio if format is False else moedas(meio)


def moedas(n=0, moeda ='R$'):
    final = f'{moeda}{n:.2f}'.replace('.', ',')
    return final

def resumo(n=0, aumento=0, reducao=0):
    print('-' * 30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<20} {moedas(n)}')
    print(f'{"Dobro do preço:":<20} {dobro(n,True)}')
    print(f'{"Metade do preço:":<20} {metade(n,True)}')
    print(f'{aumento}% {"de aumento:":<16} {aumentar(n, aumento, True)}')
    print(f'{reducao}% {"de redução:":<16} {dmimnuir(n, reducao,True)}')
    print('-' * 30)
