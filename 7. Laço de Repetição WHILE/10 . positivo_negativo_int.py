import os
os.system("clear")

nota = 0
contador = 0
soma = 0

while True:
    nota = int(input('Informe um valor inteiro: '))
    if nota < 0:
        break
    else:
        contador += 1
        soma += nota

media = soma / contador
print(f'Sua média é: {media:.1f}')