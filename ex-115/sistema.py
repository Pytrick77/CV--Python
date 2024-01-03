from biblioteca import inter, arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = inter.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa!
        inter.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = inter.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema!
        inter.cabecalho('Saindo do sistema... Até logo!!!')
        break
    else:
        # Digitou a opção errada no menu.
        print('\033[31mERRO!!! Digite uma opção válida...\033[m')
    sleep(2)
