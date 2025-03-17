import os
os.system("clear")

soma = 0 

for s in range(5):
    numero = int(input(f"Informe {s+1}º número: "))
    #soma = soma + numero
    soma += numero

    print()
    print(f"Soma {soma}")

print("FIM DA SOMA")
