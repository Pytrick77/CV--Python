def aumentar(n=0, porcen=0):
    aumento = n + (n * (porcen / 100)) 
    return aumento


def dmimnuir(n=0, porcen=0):
    menos = n - (n * (porcen / 100))
    return menos


def dobro(n=0):
    dobrar = n * 2
    return dobrar


def metade(n=0):
    meio = n / 2
    return meio


def moedas(n=0, moeda ='R$'):
    final = f'{moeda}{n:.2f}'.replace('.', ',')
    return final
