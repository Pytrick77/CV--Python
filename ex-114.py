import urllib.request

try:
    urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site não está acessível no momento\033[m')
else:
    print('\033[0;32mO site está acessível\033[m')
