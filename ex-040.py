n1= float(input('Informe a primeira nota: '))
n2= float(input('Informe a segunda nota: '))

media = (n1+n2) / 2

print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é de {media:.1f}!')

if media < 5:
    print('O aluno está REPROVADO!!')

# elif 6.9 > media >= 5:  | Outra forma de fazer a comparação...
#     print('O aluno está de RECUPERAÇÃO!')

elif media >= 5 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO!!')

elif media >= 7:
    print('O aluno está APROVADO!!')
