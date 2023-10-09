from random import randint
from time import sleep
lista = []

def sorteia():
    while len(lista) <= 4:
        numeros = randint(1, 10)
        if numeros not in lista:
            lista.append(numeros)
    print(f'Sorteando os valores da lista:', end=' ')
    sleep(0.4)


def somaPar():
    soma = 0
    for numero in lista:
        print(f'{numero}', end=' ')
        sleep(0.3)
        if numero % 2 == 0:
            soma += numero
    print(f'\nA soma dos valores pares de {lista} é {soma}.') 


sorteia()
somaPar()
