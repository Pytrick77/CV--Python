times = 'Botafogo', 'Grêmio', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG', 'Fortaleza', 'Cruzeiro', 'Internacional', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Vasco', 'América-MG'

print('*=*'*15)
print(f'Lista de time do Brasileirão: {times}')
print('*=*'*15)
print(f'Os 5 primeiros são {times[:5]}')
print('*=*'*15)
print(f'Os 4 últimos são {times[-4:]}')
print('*=*'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('*=*'*15)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição.')
