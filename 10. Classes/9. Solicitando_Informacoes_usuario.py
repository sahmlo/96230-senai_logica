import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Informacoes:
    nome: str
    idade: int
    peso: float
    altura: float
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}")

lista_de_usuario = []
QUANTIDADE_USUARIO = 4

for i in range(QUANTIDADE_USUARIO):
    usuario = Informacoes(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
        )
    lista_de_usuario.append(usuario)
    os.system("clear")

print("\n=== Dados do Usuário ===")
for usuario in lista_de_usuario:
    usuario.exibir_dados()