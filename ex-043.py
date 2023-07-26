cores = {"vermelho": "\033[30;41m" , "azul": "\033[34m", "fechamento": "\033[m" , "verde":"\033[32m" , "preto": "\033[033;40m", "amarelo": "\033[33;1m"}

print(f'{cores["vermelho"]}{"Cálculo de IMC": ^50}{cores["fechamento"]}')

peso = float(input(f'{cores["azul"]}Informe seu peso:{cores["fechamento"]} '))
altura = float(input(f'{cores["azul"]}Informe sua altura:{cores["fechamento"]} '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está com um {cores["amarelo"]}IMC de {imc:.1f}{cores["fechamento"]}, abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'Você está com um {cores["verde"]}IMC de {imc:.1f}{cores["fechamento"]}, peso ideal!')
elif 25 <= imc < 30:
    print(f'Você está com um {cores["amarelo"]}IMC de {imc:.1f}{cores["fechamento"]}, sobrepeso!')
elif 30 <= imc < 40:
    print(f'Você está com um {cores["vermelho"]}IMC de {imc:.1f}{cores["fechamento"]}, obesidade!!')
else:
    print(f'Você está com um {cores["vermelho"]}IMC de {imc:.1f}{cores["fechamento"]},  obesidade mórbida!')




