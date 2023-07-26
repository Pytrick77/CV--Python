reta1, reta2, reta3 = input('Informe 3 retas: ').split()
reta1, reta2, reta3 = float(reta1), float(reta2), float(reta3)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo!')