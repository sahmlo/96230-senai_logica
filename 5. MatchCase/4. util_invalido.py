import os
os.system ("clear")

#ENTRADA                     
dia = int(input("Digite um número: "))

#PROCESSAMENTO
match dia:
    case 1:
        print("Domingo é final de semana.")
    case 2:
        print("Segunda é um dia util")
    case 3:
        print("Terça é um dia util")
    case 4:
        print("Quarta é um dia util")
    case 5:
        print("Quinta é um dia util")
    case 6:
        print("Sexta é um dia util")
    case 7:
        print("Sábado é um dia util")
    case _:
        print("Opção Inválida.")
#SAIDA