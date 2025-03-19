import os
os.system("clear")

soma = 0
QUANTIDADE_NOTA = 2


for i in range(QUANTIDADE_NOTA):
    while True:
        nota = float(input(f"Informe a {i+1} ª nota: "))
        
        if nota < 0 or nota > 10:
            print("Tente Novamente.")
        else:
            soma+=nota
            break
print(f"Sua média é {soma / QUANTIDADE_NOTA}")
