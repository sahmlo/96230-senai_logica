import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Informacao:
    nome: str
    idade: int
    peso: float
    altura: float

nome = Informacao("Maria Clara", "20", "68.9", 1.65)

print("Exibindo Dados Cadastrado")
print(f"\nNome: {nome.nome} \nIdade: {nome.idade} \nPeso: {nome.peso} \nAltura: {nome.altura}")