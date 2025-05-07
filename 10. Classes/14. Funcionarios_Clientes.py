import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Funcionarios:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str
def exibir_dados_funcionarios (self):
    print("Nome: {self.nome} \nData de Admissão: {self.data_admissao} \nMatrícula: {self.matricula}\nEndereço: {self.endereco}\n")

@dataclass
class Clientes:
    nome: str
    data_de_nascimento: str
    endereco: str
def exibir_dados_clientes (self):
    print("Nome: {self.nome} \nData de nascimento: {self.data_de_nascimento} \nEndereço: {self.endereco}\n")

lista_de_clientes = []
lista_de_funcionarios = []
QUANTIDADE_DE_PESSOAS = 3

opcao = input ("1 - Funcionarios \n2 - Clientes \nDigite a opçao de cadastro desejada: ")
match opcao:
    case "1":
        for i in range(QUANTIDADE_DE_PESSOAS):
            proletariados = Funcionarios(nome=input("\nDigite seu nome: "), 
                                         data_admissao=input("Digite a data de Admissão: "),
                                         matricula=input("Digite sua matrícula: "),
                                         endereco=input("Digite seu endereço: \n"))
            lista_de_funcionarios.append(proletariados)
        nome_do_arquivo = "Proletariados.txt"
        with open (nome_do_arquivo, 'a') as clt_proletariados:
            for proletariados in lista_de_funcionarios:
                clt_proletariados.write(f"{proletariados.nome} \n{proletariados.data_admissao} \n{proletariados.matricula} \n{proletariados.endereco} \n")

    case "2":
        for i in range(QUANTIDADE_DE_PESSOAS):
            consumidores = Clientes(nome=input("\nDigite seu nome: "), 
                                    data_de_nascimento=input("Digite sua data de nascimento: "),
                                    endereco=input("Digite seu endereço: \n"))
            lista_de_clientes.append(consumidores)
        nome_do_arquivo = "Consumidor.txt"
        with open (nome_do_arquivo, 'a') as cliente_consumidor:
            for consumidores in lista_de_clientes:
                cliente_consumidor.write(f"{consumidores.nome} \n{consumidores.data_de_nascimento} \n {consumidores.endereco} \n")
    case _:
        print("Opção Invalida")