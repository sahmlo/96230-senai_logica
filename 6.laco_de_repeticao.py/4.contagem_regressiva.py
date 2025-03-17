import os
os.system("clear")
import time

print("Contagem Regressiva")
numero = int(input("\nInforme um número: "))

for numero in range(numero,0,-1):
    print(f"{numero}")
    time.sleep(2)

print("\nPARABÉNS ACABOU O PROGRAMA :D")