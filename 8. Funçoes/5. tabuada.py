import os
os.system("clear")

def tabuada (numero):
    multiplicao = numero * m
    
numero = int(input("Digite um número: "))
print("=== Tabuada ===")
for m in range (11):
    print(f"{numero} x {m} = {numero * m}")