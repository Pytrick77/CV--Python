print('Os números pares dentro de uma sequência de 1 a 50 são: ')

for i in range (1, 51):
    if i % 2 == 0:
        print(f'{i}' , end=(' '))

#  Outra forma de resolver o mesmo exercício com menos iterações e menos linhas

# for i in range (2, 51, 2):
#     print(i, end=(' '))
