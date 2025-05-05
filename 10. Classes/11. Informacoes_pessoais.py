import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Informacoes_funcionarios:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nRG: {self.rg} \nCPF: {self.cpf}\n")

lista_de_fucionarios = []
PESSOA = 5

for i in range(PESSOA):
    funcionarios= Informacoes_funcionarios(
                                nome=input("Digite o seu nome: "),
                                data_nascimento=input("Digite sua data de nascimento: "),         
                                rg= input("Digite seu RG: "),
                                cpf= input("Digite seu CPF: ")
                                )
    lista_de_fucionarios.append(funcionarios)
    os.system("clear")

nome_arquivo = ("Dados_funcionarios.txt")
with open(nome_arquivo, "a") as pessoas_funcionarios: 
    for funcionarios in lista_de_fucionarios:
        pessoas_funcionarios.write(f"{funcionarios.nome}, {funcionarios.data_nascimento}, {funcionarios.rg}, {funcionarios.cpf}\n")
print("DADOS SALVOS COM SUCESSO")
os.system("clear")
print("===Dados dos Funcionários===")

for funcionarios in lista_de_fucionarios:
    funcionarios.exibir_dados()