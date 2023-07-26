from math import cos, sin, tan, radians

angulo = float(input('Informe o angulo: '))

cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangen = tan(radians(angulo))

print('Dado o ângulo {}, o seno é {:.4f}, o cosseno é {:.4f}, e a tangente é {:.4f}!'.format(angulo,seno,cosseno,tangen))