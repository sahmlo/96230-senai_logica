import os
os.system("clear")

nota = 0
QUANTIDADE_NOTAS = 2

for i in range (QUANTIDADE_NOTAS):
    nota += float(input("Informe sua nota: "))
    def media (nota):
        nota_media = nota / 2
        return nota_media
    
    def aprovado_reprovado (nota_media):
        if nota_media >= 7:
            return "Aprovado. Parabéns!"
        else:
            return "Reprovado, tente novamente."

media_estudante = media(nota)
estudante = aprovado_reprovado(media_estudante)

print(f"Sua média é {media_estudante}.")
print(f"{estudante}")