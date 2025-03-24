import os
os.system("clear")

contador = 0
nota = 0

while True:
    contador += 1
    nota += int(input("\nInforme sua nota: "))
    continuar = input("\nDeseja inserir outra nota? (S/N): ").lower()
    if continuar == "n":
        print(f"\nSua Média é: {nota/contador:.2f}")
        break



