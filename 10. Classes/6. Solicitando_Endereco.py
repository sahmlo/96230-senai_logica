import os
from dataclasses import dataclass
os.system("clear")

@dataclass 
class Endereco:
    logradouro: str
    numero: str
    cidade: str
@dataclass
class Dados():
    nome: str
    email: str
    endereco: Endereco
    def exibindo_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nLogradouro: {self.endereco.logradouro} \nNúmero: {self.endereco.numero} \nCidade: {self.endereco.cidade}")

nome = input("Informe seu nome: ")
email = input("Informe seu e-mail: ")
logradouro = input("Informe seu endereço: ")
numero = input("Informe o número: ")
cidade = input("Informe sua cidade: ")

endereco = Endereco(logradouro, numero, cidade)
dados1 = Dados(nome, email, endereco)

os.system("clear")
print("\n=== Exibindo Dados ===")
dados1.exibindo_dados()