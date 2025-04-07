import os
os.system("clear")

def par_impar (numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("Digite um número: "))
resultado = par_impar(numero)

print("O número digitado é {resultado}")