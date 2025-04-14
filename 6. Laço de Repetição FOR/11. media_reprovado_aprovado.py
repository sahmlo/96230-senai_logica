
#LIMPAR O TERMINAL.
import os
os.system("clear")

media = 0 

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    media += nota
if media / 3 >= 7:
    print(f"APROVADO, PARABÉNS!")
elif media / 3 >= 4:
    print("RECUPERAÇÃO")
elif media / 3 < 4:
    print("REPROVADO!")

print