import os
os.system("clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

def positivos_negativos(lista):
    positivos = 0
    negativos = 0
    soma_positivo = 0
    for numero in lista:
        if numero >= 0:
            positivos += 1
            soma_positivo += numero
        else:
            negativos += 1
    return positivos, negativos, soma_positivo

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

positivos, negativos, soma_positivo = positivos_negativos(lista_numeros)

print("\nMostrando números")
for i, numero in enumerate(lista_numeros, 1):
    print(f"{i}º número: {numero}")

print(f"A soma dos números positivo: {soma_positivo}")
print(f"\nQuantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")

            