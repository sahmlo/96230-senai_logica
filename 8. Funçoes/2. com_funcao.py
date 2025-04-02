import os
os.system("clear")

def calcular_media (primeiro_nota, segundo_nota):
    soma = primeiro_numero + segundo_numero
    media = soma /2
    return media

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

media = calcular_media(primeiro_numero, segundo_numero)

print(f"Média: {media}")
