import os
os.system("clear")



nota = 0

for i in range(3):
    nota += float(input("Informe sua nota: "))

if nota >= 7:
    print(f"Sua média é: {nota/3}")
    print("Aprovado!")
elif nota <= 4:
    print(f"Sua média é: {nota/3}")
    print("Recuperação.")
else:
    print(f"Sua média é: {nota/3}")
    print("Reprovado!")

