import os
os.system("clear")

nota = 0
QUANTIDADE_NOTAS = 3

for i in range (QUANTIDADE_NOTAS):
    nota += float(input("Informe sua nota: "))
    def media (nota):
        nota_media = nota / 3
        return nota_media
    
media_estudante = media(nota)

print(f"Sua média é {media_estudante}. Parabéns")