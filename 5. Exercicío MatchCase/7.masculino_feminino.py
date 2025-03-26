import os
os.system ("clear")

#ENTRADA
resultado = input("Informe seu gênero \nM - Masculino \nF - Feminino \nInforme a opção desejada: ").upper()
altura = float(input("Digite sua altura: "))

match resultado:
    case "M" | 'm':
        peso = (72.7 * altura) - 58
        print(f"Seu peso ideal é {peso:.2f}")
    case "F" | 'f':
        peso = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é {peso:.2f}")

    case _:
        print("Opção Inválida.")
