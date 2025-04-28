import os
from dataclasses import dataclass
os.system("clear")

@dataclass 
class Endereco:
    logradouro: str
    numero: int
@dataclass
class Pessoas():
    nome: str
    idade: int
    endereco: Endereco
    def exibindo_dados(self):
        print("=== Dados Pessoais ===")
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nLogradouro: {self.endereco.logradouro} \nNúmero: {self.endereco.numero}")

endereco1 = Endereco("Rua A", "33")
pessoa1 = Pessoas ("Marta", 22, endereco1)

pessoa1.exibindo_dados()