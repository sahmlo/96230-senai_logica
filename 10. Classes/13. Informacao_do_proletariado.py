import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

def exibir_dados(self):
    print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nRG: {self.rg} \nCPF: {self.cpf}\n")

informacoes_funcionarios = []
PESSOA = 5

for i in range(PESSOA):
    funcionario= Funcionario(
                            nome = input("Digite o seu nome: "),
                            data_nascimento = input("Digite sua data de nascimento: "),         
                            rg = input("Digite seu RG: "),
                            cpf = input("Digite seu CPF: ")
                            )
    informacoes_funcionarios.append(funcionario)
    os.system("clear")                         

arquivo_nome = ("Funcionarios.txt")
with open (arquivo_nome, "a") as funcionarios_pessoas:
    for funcionarios in informacoes_funcionarios:
        funcionarios_pessoas.write(f"{funcionarios.nome}, {funcionarios.data_nascimento}, {funcionarios.rg}, {funcionarios.cpf}\n")
print("DADOS SALVOS COM SUCESSO")
os.system("clear")
print("=== Dados dos Funcionários ===\n")
print("EXIBINDO ARQUIVO\n")

try:
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())    
except FileNotFoundError:
    print("Arquivo não encontrado.")