import os
os.system("clear")
numero = float(input("Informe o valor para conversão em centímetros: "))

def metro_centimetro (numero):
    conversao = numero * 100
    return conversao
    # return numero * 100;

centimetro = metro_centimetro(numero)
#centimetro = metro_centimetro(numero)


print(f" {centimetro:.0f} centímetros.")



