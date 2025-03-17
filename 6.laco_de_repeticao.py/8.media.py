import os
os.system("clear")

media = 0

for i in range(4):
    nota = float(input("Informe sua nota: "))
    media += nota

#media = soma / 4

print(f"Sua média é: {media/4}")