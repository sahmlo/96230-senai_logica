import os
os.system("clear")

login = "sara"
senha = "123456"
contador = 0

while True:
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")
    if login == "Sara" and senha == "123456":
        print("Acesso Permitido.")
        break
    else:
        print("login ou senha invalidos. \n")
        contador += 1
    if contador == 3:
            print("Tentativas acima do permitido.")
            break