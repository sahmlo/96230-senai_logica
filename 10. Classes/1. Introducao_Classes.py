import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Pessoas:
    nome: str
    idade: int
@dataclass
class Pet:
    nome:str
    idade:int
    raca:str

pessoa1 = Pessoas("Larissa", 20)
pessoa2 = Pessoas("Nadson", 20 )

pet1= Pet("Salém", 4, "gato preto")
pet2= Pet("Luci", 4, "gato cinza")

print("Dados das Pessoas")
print(f"\nNome: {pessoa1.nome} \nIdade: {pessoa1.idade}")
print(f"\nNome: {pessoa2.nome} \nIdade: {pessoa2.idade}")

print("\nDados dos Pets")
print(f"\nNome: {pet1.nome} \nIdade: {pet1.idade} \nRaça: {pet1.raca}")
print(f"\nNome: {pet2.nome} \nIdade: {pet2.idade} \nRaça: {pet2.raca}")