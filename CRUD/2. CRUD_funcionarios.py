import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    cpf: str
    cargo: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nCPF: {self.cpf} \nCargo: {self.cargo}")

dados_funcionarios = []

def verificar_lista_vazia(dados_funcionarios):
    if not dados_funcionarios:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar_dados_lista(dados_funcionarios):
    os.system("clear")
    nome = input("Digite o nome do funcionário: ")
    data_nascimento = input("Digite a data de nascimento do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    funcionario = Funcionario(nome, data_nascimento, cpf, cargo)
    dados_funcionarios.append(funcionario)
    print(f"\nFuncionário {funcionario.nome} adicionado com sucesso.")

def mostrar_dados(dados_funcionarios):
    if verificar_lista_vazia(dados_funcionarios):
        input("\nPressione Enter para voltar ao menu")  # Adicionado aqui!
        return
    os.system("clear")
    print("\n - Lista de Funcionários - ")
    for funcionario in dados_funcionarios:
        funcionario.exibir_dados()
        print("-" * 30)
    input("\nPressione Enter para voltar ao menu")

def atualizar_dados(dados_funcionarios):
    os.system("clear")
    if verificar_lista_vazia(dados_funcionarios):
        return
    mostrar_dados(dados_funcionarios)
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")
    for funcionario in dados_funcionarios:
        if funcionario.nome == nome_antigo:
            novo_nome = input(f"Digite o novo nome para {nome_antigo}(ou ENTER p/ manter): ").lowwer() or funcionario["nome"]
            nova_data_nascimento = input(f"Digite a nova data de nascimento para {nome_antigo} (ou ENTER p/ manter): ") or funcionario["data_nascimento"]
            novo_cpf = input(f"Digite o novo CPF para {nome_antigo} (ou ENTER p/ manter): ") or funcionario["cpf"]
            novo_cargo = input(f"Digite o novo cargo para {nome_antigo} (ou ENTER p/ manter): ") or funcionario["cargo"]
            funcionario.nome = novo_nome
            funcionario.data_nascimento = nova_data_nascimento
            funcionario.cpf = novo_cpf
            funcionario.cargo = novo_cargo
            print(f"\nDados do funcionário {nome_antigo} atualizados com sucesso.")
            return
    print(f"\nO funcionário {nome_antigo} não foi encontrado.")

def excluir_dados(dados_funcionarios):
    os.system("clear")
    if verificar_lista_vazia(dados_funcionarios):
        return
    mostrar_dados(dados_funcionarios)
    nome_remover = input("Digite o nome do funcionário que deseja remover: ")
    for funcionario in dados_funcionarios:
        if funcionario.nome == nome_remover:
            dados_funcionarios.remove(funcionario)
            print(f"\nFuncionário {nome_remover} removido com sucesso.")
            return
    print(f"\nO funcionário {nome_remover} não foi encontrado.")

while True:
    os.system("clear")
    print("""=== BEM-VINDO ===

1 - Adicionar dados
2 - Listar dados
3 - Atualizar dados
4 - Remover dados
5 - Sair           
    """)
    try:
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                adicionar_dados_lista(dados_funcionarios)
            case 2:
                mostrar_dados(dados_funcionarios)
            case 3:
                atualizar_dados(dados_funcionarios)
            case 4:
                excluir_dados(dados_funcionarios)
            case 5:
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")