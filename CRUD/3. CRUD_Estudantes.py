import os
from dataclasses import dataclass

os.system("clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str

    def exibir_endereco(self):
        print(f"Endereço: {self.logradouro}, {self.numero} - {self.cidade}/{self.estado}")

@dataclass
class Aluno:
    nome: str
    data_nascimento: str
    ra: str
    curso: str
    endereco: Endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nR.A: {self.ra} \nCurso: {self.curso}")
        self.endereco.exibir_endereco()

dados_alunos = []

def verificar_lista_vazia(dados_alunos):
    if not dados_alunos:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar_dados_lista(dados_alunos):
    os.system("clear")
    nome = input("Digite o nome do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno: ")
    ra = input("Digite o R.A do aluno: ")
    curso = input("Digite o curso do aluno: ")

    print("\n--- Endereço ---")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    endereco = Endereco(logradouro, numero, cidade, estado)
    aluno = Aluno(nome, data_nascimento, ra, curso, endereco)
    dados_alunos.append(aluno)
    print(f"\nAluno {aluno.nome} adicionado com sucesso.")

def mostrar_dados(dados_alunos):
    if verificar_lista_vazia(dados_alunos):
        input("\nPressione Enter para voltar ao menu: ")  
        return  
    os.system("clear")  
    print("\n - Lista de Alunos - ")
    for aluno in dados_alunos:
        aluno.exibir_dados()
        print("-" * 30)
    input("\nPressione Enter para voltar ao menu: ") 

def atualizar_dados(dados_alunos):
    os.system("clear")
    if verificar_lista_vazia(dados_alunos):
        return
    mostrar_dados(dados_alunos)
    nome_antigo = input("Digite o nome do aluno que deseja atualizar: ")
    for aluno in dados_alunos:
        if aluno.nome == nome_antigo:
            novo_nome = input(f"Digite o novo nome para {nome_antigo} (ou ENTER p/ manter): ") or aluno.nome
            nova_data_nascimento = input(f"Digite a nova data de nascimento para {nome_antigo} (ou ENTER p/ manter): ") or aluno.data_nascimento
            novo_ra = input(f"Digite o novo R.A para {nome_antigo} (ou ENTER p/ manter): ") or aluno.ra
            novo_curso = input(f"Digite o novo curso para {nome_antigo} (ou ENTER p/ manter): ") or aluno.curso

            print("\n--- Atualizar Endereço ---")
            novo_logradouro = input(f"Digite o novo logradouro (ou ENTER p/ manter): ") or aluno.endereco.logradouro
            novo_numero = input(f"Digite o novo número (ou ENTER p/ manter): ") or aluno.endereco.numero
            nova_cidade = input(f"Digite a nova cidade (ou ENTER p/ manter): ") or aluno.endereco.cidade
            novo_estado = input(f"Digite o novo estado (ou ENTER p/ manter): ") or aluno.endereco.estado

            aluno.nome = novo_nome
            aluno.data_nascimento = nova_data_nascimento
            aluno.ra = novo_ra
            aluno.curso = novo_curso
            aluno.endereco = Endereco(novo_logradouro, novo_numero, nova_cidade, novo_estado)

            print(f"\nDados do aluno {nome_antigo} atualizados com sucesso.")
            return
    print(f"\nO aluno {nome_antigo} não foi encontrado.")

def excluir_dados(dados_alunos):
    os.system("clear")
    if verificar_lista_vazia(dados_alunos):
        return
    mostrar_dados(dados_alunos)
    nome_remover = input("Digite o nome do aluno que deseja remover: ")
    for aluno in dados_alunos:
        if aluno.nome == nome_remover:
            dados_alunos.remove(aluno)
            print(f"\nAluno {nome_remover} removido com sucesso.")
            return
    print(f"\nO aluno {nome_remover} não foi encontrado.")

while True:
    os.system("clear")
    print("""=== BEM-VINDO ===

1 - Adicionar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Remover aluno
5 - Sair           
    """)
    try:
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                adicionar_dados_lista(dados_alunos)
            case 2:
                mostrar_dados(dados_alunos)
            case 3:
                atualizar_dados(dados_alunos)
            case 4:
                excluir_dados(dados_alunos)
            case 5:
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")