import os
os.system ("clear")

aluno = input('Informe seu nome: ')
nota_um = float(input('Informe sua primeira nota: '))
nota_dois = float(input('Informe sua segunda nota: '))

media = (nota_um + nota_dois) / 2

if media >= 9:
    conceito = "A"
elif media > 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"
match conceito:
    case "A" | "B" | "C":
        print(f"Conceito: {conceito}")
        print("Aprovado")
    case  "D" | "E":
        print(f"Conceito: {conceito}")
        print("REPROVADO")
    case _:
        print("Opção inválida.")