alunos_nota = []
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos_nota.append([nome,[nota1, nota2], media])
    continuar = str(input('Continuar? [S/N]')).upper()[0].strip()
    if continuar in 'N':
        break
print('+=+=' * 25)
print(f'{"N°":<4}{"Aluno":<8}{"Média":>10}')
print('-' * 26)
for i, aluno in enumerate(alunos_nota):
    print(f'{i:<4}{aluno[0]:<8}{aluno[2]:>10}')
print('-=-=' * 25)
while True:
    print('-' * 35)
    opcao = int(input('Digite o N° do aluno para ver as notas (999 para interromper): '))
    if opcao == 999:
        break
    if opcao <= len(alunos_nota) - 1:
        print(f'As notas do aluno {alunos_nota[opcao][0]} foram: {alunos_nota[opcao][1]}!')
print('Obrigado por usar o programa!!')
