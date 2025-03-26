import os
os.system("clear")

par = 0
impar = 0

for i in range(5):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    
print(f"\nNúmeros Pares:{par} \nNúmeros Impares: {impar}")