def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    # print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return f'Com {idade} anos: Voto Negado!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional!'
    else:
        return f'Com {idade} anos: Voto Obrigatório!'


print('-' * 35)
usuario = int((input('Digite seu ano de nascimento: ')))
print(voto(usuario))
