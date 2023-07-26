nome = str(input('Escreva seu nome completo: ')).strip()
espaco = nome.count(' ') ; caracteres = len(nome)
todo = caracteres -  espaco  
lista = nome.split()
primeiro_nome = len(lista[0])


print('Analisando os dados...')
print('-'*30)
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras!'.format(todo))
print('O primeiro nome {} tem {} letras.'.format(lista[0] ,primeiro_nome))
print('-'*30)

# Outra forma de achar quantas letras tem o primeiro nome, um jeito ainda mais fácil.

print(nome.find(' '),'letras')