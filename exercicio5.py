#Exercicio5
#Cauan K, 09/13/17
#Kill me please

c = input("Digite o valor de C: \n")
n_String = input("Digite o valor de N: \n")

n = int(n_String)

if(n > 50):
    n2 = 50
    salario = 10 * n2

    ne = n - 50
    e = ne * 20

else:
    salario = 10 * n
    e = 0

salarioTotal = salario + e

print("\n O salário total: R$ " + str(salarioTotal))
print("\n O salário excedente: R$ " + str(e))

