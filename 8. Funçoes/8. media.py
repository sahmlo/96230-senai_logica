import os
os.system("clear")

def nota_media (primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero
    media = soma /2
    return media

def maior_ou_menor (media):
    if media >= 7:
        return "Aprovado."
    else:
        return "Reprovado."

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

media = nota_media(primeiro_numero, segundo_numero)
aprovado_reprovado = maior_ou_menor (media)

print(f"Média: {media}")
print(f"Você está {aprovado_reprovado}")