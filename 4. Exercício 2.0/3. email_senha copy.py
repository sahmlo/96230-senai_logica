import os
os.system ("clear")


#VAR

login_cadastrado = ("Amanda")
senha_cadastrada = ("212004")

#entrada

login = input ("Login: ")
senha = input ("Senha: ")

#solitando dados
if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem Vindo!")
else: 
    print("Login ou senha inválidos.")



