import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Pessoas:
    nome: str
    idade: int
    peso: float
    altura: float

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa1 = Pessoas (nome=nome, idade=idade, peso=peso, altura=altura)
#pessoa2 =Pessoas (nome, idade,peso,altura)

print("=== Dados Pessoais ===")
print(f"\nNome: {pessoa1.nome} \nIdade: {pessoa1.idade} \nPeso: {pessoa1.peso} \nAltura: {pessoa1.altura:.2f}")