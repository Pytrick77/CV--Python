from time import sleep

def maior(* numeros):
    print('-+-+' * 10)
    print(f'Analisando os valores passados...')
    maior = 0
    for num in numeros:
        print(num, end=' ')
        sleep(1)
        if num > maior:
            maior = num
    print(f'Foram informados {len(numeros)} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    sleep(1)
    print()


maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(2, 1)
maior(6)
maior()
