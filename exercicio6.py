#Exercicio6
#Cauan K, 09/13/17
#The last one

import math

alturaCilindro = input("Insira a altura (em metros) do cilindro: \n")
raioCilindro = input("Insira o raio (em metros) do cilindro: \n")

altura = int(alturaCilindro)
raio = int(raioCilindro)

areaBase = math.pi * math.pow(raio, 2)

areaLateral = 2 * math.pi * raio * altura

areaTotal = 2 * areaBase + areaLateral

QTDE = areaTotal / 3

QTDE_Cheia = QTDE / 5

C = QTDE * 50

print("\n Qtd de latas de tinta (cheias): " + str(QTDE_Cheia))
print("\n Custo total: " + str(C))