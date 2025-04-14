import os
os.system("clear")

#Elabore um algoritmo para solitar dois números e ao final mostre na tela:
#A média, a soma, o produto, o menor valor e o maior valor.
#Usando uma linha para cada resultado

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))


#media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
media = soma /2

produto = primeiro_numero * segundo_numero

menor =min(primeiro_numero, segundo_numero)
maior =max(primeiro_numero, segundo_numero)

print("\nExibindo resultado: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")