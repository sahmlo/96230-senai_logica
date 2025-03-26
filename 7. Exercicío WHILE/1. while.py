import os
os.system("clear")
contador = 0
continua = 's'

while continua == 's':
    print("Repetindo...")

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()

    contador +=1

if contador == 0:
    print("O bloco NÃO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes.")
