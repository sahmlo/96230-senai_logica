import os
os.system("clear")

#Elabore um algoiritmo para solicitar ao usuário três notas.
#Calcule a média do estudante
#Caso a média do estudante seja menor que 7, o número está reprovado 
#Mostrar: média e se está aprovado ou reprovado.

#ENTRADA 

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a treceira nota: "))

soma = nota_um + nota_dois + nota_tres
media = soma / 3

#SOLITANDO DADOS

print(f"Média: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado!")

