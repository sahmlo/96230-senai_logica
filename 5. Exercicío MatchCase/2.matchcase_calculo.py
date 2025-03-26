import os
os.system ("clear")

#ENTRADA
primeiro_numero = int(input("Digite um número: "))
operador = input("Digite a operação (+ - * /): ")
segundo_numero = int(input("Digite um número: "))

#PROCESSAMENTO
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = "Opção inválida"
#SAIDA
print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Operação: {operador}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")
