import os
os.system ("clear")

#ENTRADA
idade = int(input("Digite sua idade: "))

#SOLICITANDO DADOS
if idade >= 18 and idade <= 65: 
    print("É obrigado a votar.")
else:
    print("Não é obrigado a votar.")