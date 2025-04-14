import os
os.system("clear")

#Criando uma lista.
lista_de_nota = []

#Adicionado 3 notas em lista.
for i in range(3):
    nota = float(input("Informe sua nota: "))
    lista_de_nota.append(nota)

#Exibindo todos os valores em uma lista
print()
for nota in lista_de_nota: #ForEach
    print(nota)