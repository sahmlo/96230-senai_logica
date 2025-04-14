import os
os.system ("clear")

dia = input("Digite dias da semana: ")

match dia:
    case "segunda":
        print("Hoje é segunda-feira.")
    case "terça":
        print("Hoje é terça-feira.")
    case "quarta":
        print("Hoje é quarta-feira.")
    case "quinta":
        print("Hoje é quinta-feira.")
    case "sexta":
        print("Hoje é sexta-feira.")
    case "sábado" | "domingo":
        print("Hoje é fianl de semana.")

    case _:
     print("Dia invalido")

print(dia)

print("=== FIM ===")
