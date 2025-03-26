import os
os.system("clear")

login = "Sara"
senha = "123456"

while True:
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

    if login == "Sara" and senha == "123456":
        break
    else:
        print("login ou senha invalidos.")

print("Acesso Permitido.")