def notas(* n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias);
    :param sit: valor opcional, indicando se deve ou não adicionar a situação;
    :return: dicionário com várias informações sobre a situação da turma. 
    '''
    nota = {}
    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['media'] = sum(n) / len(n)
    if sit:
        if nota['media'] > 7:
            nota['situação'] = 'Boa' 
        elif 5 <= nota['media'] < 7:
            nota['situação'] = 'RAZOÁVÁEL' 
        else:
            nota['situação'] = 'RUIM' 
    return nota
    

resultado = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resultado)
help(notas)
