import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Pessoas():
    nome: str
    email: str
    telefone: str
    endereco: str
    def exibindo_dados(self):
        print("\n=== Dados Pessoais ===")
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone} \nEndereço: {self.endereco}")

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

pessoa1 = Pessoas (nome, email, telefone, endereco)
pessoa1.exibindo_dados()