import os
os.system("clear")
numero = int(input("Informe um número: "))
def positivo_negativo (numero) :
    if numero > 0:
        print("Esse número é positivo.")
    elif numero == 0:
        print("Esse número é neutro.")
    else:
        print("Esse número é negativo.")

resultado = positivo_negativo (numero)

