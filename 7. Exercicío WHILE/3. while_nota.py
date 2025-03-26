import os
os.system("clear")

while True:
    nota = float(input("Digite sua sua nota: "))
    if nota < 0 or nota > 10:
        print("Digite sua nota novamente \n")

    else:
        break    

print(f"Nota {nota}")