import os
os.system("clear")

while True:
    nota1 = float(input("Informe a 1ª nota: "))
    nota2 = float(input("Informe a 2ª nota: "))
    
    if nota1 < 0 or nota1 > 10:
        print("Tente Novamente a primeira nota.")
    elif nota2 < 0 or nota2 > 10:
        print("Tente Novamente a segunda nota.")
    else:
        break
print(f"Sua média é {(nota1+nota2)/2}")
