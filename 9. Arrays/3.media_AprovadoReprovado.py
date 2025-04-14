import os
os.system("clear")

lista_de_nota = []
QUANTIDADE_DE_NOTAS = 4

for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f"Informe {i+1}ª nota: "))
    lista_de_nota.append(nota)
print()
for nota in lista_de_nota: 
    print(nota)
media = sum(lista_de_nota)/QUANTIDADE_DE_NOTAS
if media < 5:
    print(f"\nMédia: {media} Reprovado")
elif 7 > media > 5:
    print(f"Média: {media} Recuperação")
elif media >= 7:
    print(f"Média: {media} Aprovado")