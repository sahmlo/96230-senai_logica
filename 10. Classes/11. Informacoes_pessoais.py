import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Informacôes_pessoas:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nRG: {self.rg} \nCPF: {self.cpf}\n")

imformacoes_pessoas = []
PESSOA = 5

for i in range(PESSOA):
    funcionarios= Informacôes_pessoas(
                                nome=input("Digite o seu nome: "),
                                data_nascimento=input("Digite sua data de nascimento: "),         
                                rg= input("Digite seu RG: "),
                                cpf= input("Digite seu CPF: ")
                                )
    imformacoes_pessoas.append(funcionarios)
    os.system("clear")

nome_arquivo = ("Dados_funcionarios,txt")
with open(nome_arquivo, "a") as pessoas_funcionarios: 
    for funcionarios in imformacoes_pessoas:
        pessoas_funcionarios.write(f"{funcionarios.nome}, {funcionarios.data_nascimento}, {funcionarios.rg}, {funcionarios.cpf}\n")
print("DADOS SALVOS COM SUCESSO")
os.system("clear")
print("===Dados dos Funcionários===")

for funcionarios in imformacoes_pessoas:
    funcionarios.exibir_dados()