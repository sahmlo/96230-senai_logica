import os
os.system("clear")



media = 0

for i in range(3):
    nota = float(input("Informe sua nota: "))
    media += nota

if media >= 7:
    print(f"Sua média é: {media/3}")
    print("Aprovado!")
else:
    print(f"Sua média é: {media/3}")
    print("Reprovado!")

