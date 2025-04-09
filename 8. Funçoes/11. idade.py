import os
os.system("clear")

ano_de_nascimento = int(input("Informe o ano que você nasceu: "))

def idade (ano_de_nascimento):
    calculo_idade = 2025 - ano_de_nascimento
    return calculo_idade

idade_usuario = idade (ano_de_nascimento)
print(f"Sua idade é: {idade_usuario}")


