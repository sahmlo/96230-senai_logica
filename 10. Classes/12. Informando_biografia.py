import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    
    def exibir_dados(self):
        print("\nExibindo Dados")
        print(f"\nNome do autor: {self.autor.nome} \nTitulo do livro: {self.titulo} \nAno de publicação: {self.ano}")


autor = Autor(
    nome=input("Informe o nome do autor(a): "),
    biografia=input("Informe a biografia do autor: ")
             )

livro = Livro(
    titulo=input("Informe o nome do livro: "),
    ano=int(input("Informe o ano de publicação: ")),
    autor=autor
             )
nome_arquivo = "Informação_do_livro.txt"
with open(nome_arquivo, "a") as arquivo_livro:
    arquivo_livro.write(f"{livro.autor.nome}, {livro.titulo}, {livro.ano}\n")
    
os.system("clear")
livro.exibir_dados()