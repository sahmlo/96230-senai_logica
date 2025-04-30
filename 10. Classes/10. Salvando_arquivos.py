import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float
    def exibir_informacao(self):
        print(f"\nNome: {self.nome} \nAutor {self.autor} \nCategoria: {self.categoria} \nPreço: {self.preco}")

lista_de_livros = []
QUANTIDADE_LIVROS = 1

for i in range(QUANTIDADE_LIVROS):
    informacao_livros = Livros(
        nome = input("\nInforme o livro desejado: "),
        autor = input("Informe o autor do livro: "),
        categoria = input("Informe categoria do livro: "),
        preco = float(input("Informe o livro desejado: "))
        )
lista_de_livros.append(informacao_livros)

nome_arquivo = "Dados_do_Livro.txt"
with open(nome_arquivo, "a") as arquivos_livros:
    for informacao_livros in lista_de_livros:
        arquivos_livros.write(f"{informacao_livros.nome}\n, {informacao_livros.autor}\n, {informacao_livros.categoria}\n, {informacao_livros.preco}\n")

print("Informações sobre os livros desejados")
for informacao_livros in lista_de_livros:
    informacao_livros.exibir_informacao()