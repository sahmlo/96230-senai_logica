import os
os.system("clear")

lista_maior_menor = []

for i in range (5):
    numeros = int(input(f"Informe {i+1}ª número: "))
    lista_maior_menor.append(numeros)
print(lista_maior_menor)
maior = max(lista_maior_menor)
menor = min(lista_maior_menor)

print("\nMostrando Números")
for i, numeros in enumerate(lista_maior_menor, start= 1):
    print(f"{i}° número: {numeros}")
lista_maior_menor.reverse()

print(f"\nNúmeros maiores: {maior}")
print(f"Números menores: {menor}")