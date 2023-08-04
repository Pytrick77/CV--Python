from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

contador = False

while not contador:

    opcao = int(input('''[1] somar
[2] multiplicar                        
[3] maior                  
[4] novos números                 
[5] sair do programa
Qual é a sua opção: '''))
    
    if opcao == 1:

        soma = num1 + num2
        print(f'A soma do {num1} e do {num2} é igual á {soma}.')

    elif opcao == 2:

        mult = num1 * num2
        print(f'A multiplicação do {num1} e do {num2} é igual á {mult}.')

    elif opcao == 3:

        if num1 > num2:
            maior = num1
            print(f'O número {maior} é maior.')

        elif num2 > num1:
            maior = num2
            print(f'O número {maior} é maior.')

        else:
            print('Os dois números são iguais.')

    elif opcao == 4:
        print('Informe os números novamente.')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))

    elif opcao == 5:
        contador = True
        print('Finalizando...')
        sleep(2)

    else:
        print('Opção inválida. Tente novamente.')
        
    print(f"{'=*=*' * 10}")
    
print('Obrigado por usar o programa. Volte sempre!')
