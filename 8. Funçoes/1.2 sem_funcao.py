import os
 
#Função sem retorno
def logo_senai():
    os.system("clear")
    print("==SENAI==")

logo_senai() # Chamando função
nome = input("Digite seu nome: ")

logo_senai() # Chamando função
idade = input("Digite sua idade: ")

logo_senai() # Chamando função
print("==SENAI==")
print(f"Nome {nome}")
print(f"idade {idade}")
