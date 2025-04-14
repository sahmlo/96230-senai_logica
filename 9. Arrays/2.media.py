import os
os.system("clear")

lista_de_nota = []
QUANTIDADE_DE_NOTAS = 3

for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f"Informe {i+1}ª nota: "))
    lista_de_nota.append(nota)

media = sum(lista_de_nota)/QUANTIDADE_DE_NOTAS

print()
for nota in lista_de_nota:
    print(nota)

print("\n=== Exibindo Média ===")
print(f"Média: {media}")