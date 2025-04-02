import os
os.system("clear")

def logo_senai(): 
    os.system("clear")
    print("=== SENAI DENDEZEIROS ===")

def calcular_soma (primeiro_nota, segundo_nota): # a tradução de (def) é definir uma função.
    soma = primeiro_numero + segundo_numero
    return soma
def calcular_subtracao (primeiro_nota, segundo_nota):
    subtracao = primeiro_numero - segundo_numero
    return subtracao
def calcular_multiplicacao (primeiro_nota, segundo_nota):
    multiplicao = primeiro_numero * segundo_numero
    return multiplicao
def calcular_divisao (primeiro_nota, segundo_nota):
    divisao = primeiro_numero / segundo_numero
    return divisao

logo_senai()
primeiro_numero = int(input("\nDigite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

soma = calcular_soma(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)
multiplicacao = calcular_multiplicacao(primeiro_numero, segundo_numero)
divisao = calcular_divisao(primeiro_numero, segundo_numero)

print(f"\nSoma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.0f}")
