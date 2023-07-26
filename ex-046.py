from time import sleep
import emoji

print(f'{"O estouro dos fogos começa em...":^100}')

for i in range (10,-1,-1):
    print(i)
    sleep(1)

print(emoji.emojize(':fireworks:'*10))
