import os
os.system("clear")


QUANTIDADE_NOTAS = (3)
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Informe sua nota: "))
        if nota < 0 or nota > 10:
            print('Nota inválida. \nTente Novamente.')
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

if nota >= 7:
    total = "Aprovado. Parabéns!"
elif nota >= 5:
    
    total = "Recuperação."
else:
    total = "Reprovado."

print(f"\nSua média é: {media}")
print(f"Seu status é: {total}")
