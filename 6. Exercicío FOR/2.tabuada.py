import os
os.system("clear")
numero = int(input("Digite um número: "))
print("Tabuada")
for m in range (1,11): #range(int) executa do 0 até o número escolhido. 
    print(f"{numero} x {m} = {numero * m}")

print("FIM DO PROGRAMA")
    