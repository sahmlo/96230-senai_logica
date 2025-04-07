import os
os.system("clear")

def saudacao(parametro): 
    print(f"Olá, {parametro}! Bem-vinda(o) ao nosso site.")

nome_visitante = input('Digite seu nome: ')
saudacao(nome_visitante)


