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

#Atribuindo dados ao paciente.
paciente1 = Paciente(
                    nome = input("Digite seu nome: "), 
                    idade = int(input("Digite sua idade: ")))
#Exibindo dados do paciente.
paciente1.exibir_dados()