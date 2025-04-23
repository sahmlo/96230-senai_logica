import os
os.system("clear")

lista = []
QUANTIDADE_VETORES = 5

def vetores(numero):
    if numero < 0:
        numero = 0
    lista.append(numero)

for i in range(QUANTIDADE_VETORES):
    numero = int(input(f'Informe {i+1}º número: '))
    vetores(numero)

print(f"Valores do vetor: {lista}")