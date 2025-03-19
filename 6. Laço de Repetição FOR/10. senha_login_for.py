import os
os.system("clear")

login = "sara"
senha = "123456"


for a in range(3):
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")
    if login == "Sara" and senha == "123456":
        print("Acesso Permitido.")
        break
    else:
        print("login ou senha invalidos. \n")
        if a == 2:
            print("Tentativas acima do permitido.")