#Exercicio 2
#Made by Cauan K, 09/13/17

import math

px_String = input("Digite o valor de P no eixo X: \n")
py_String = input("Digite o valor de P no eixo Y: \n")
qx_String = input("Digite o valor de Q no eixo X: \n")
qy_String = input("Digite o valor de Q no eixo Y: \n")

px = int(px_String)
py = int(py_String)
qx = int(qx_String)
qy = int(qy_String)

if py > qy:
    catetoQR = py - qy

else:
    catetoQR = qy - py

if px > qx:
    catetoPR = px - qx

else:
    catetoPR = qx - px

distancia = math.sqrt(math.pow(catetoPR, 2) + math.pow(catetoQR, 2))

print(distancia)

