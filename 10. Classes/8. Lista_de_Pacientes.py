import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Paciente:
    #Atributos: são variáveis que pertencem a classe.
    nome: str
    idade: int

    #Métodos: é uma função que pertence a classe.
    #Este método para exibir dados do paciente.
    def exibir_dados(self):
        print(f"\nNome: {self.nome} \nIdade: {self.idade}")

#Criando uma lista de pacientes
lista_paciente = []
QUANTIDADE_PACIENTE = 2

#Atribuindo dados ao paciente.
for i in range(QUANTIDADE_PACIENTE):
    paciente = Paciente(
                    nome = input("Digite seu nome: "), 
                    idade = int(input("Digite sua idade: ")))
    lista_paciente.append(paciente)

# Salvando em um arquivo com .txt
nome_arquivo = "Dados_paciente.txt"
with open(nome_arquivo, "w") as arquivo_pacientes: 
#A palavra "w" é para substituir os dados que foi insirido.
#A palavra "a" é para acumular os dados que foi insirido.
    for paciente in lista_paciente:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")

print("Dados salvos com sucesso!")

#Exibindo dados do paciente.
print("=== Exibindo dados do Usuário ===")
for paciente in lista_paciente:
    paciente.exibir_dados()