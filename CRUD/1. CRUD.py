import os
import time

os.system("cls || clear")

# Lista de nomes.
lista_nomes = []

# Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")

# Função para mostar todos os nomes da lista.
def mostrar_nomes(lista_nomes):
    # Vefificar se a lista está vazia.
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return

    print("\n - Lista de nomes - ")
    for nome in lista_nomes:
        print(f"- {nome}")

# Função para excluir.
def excluir_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return

    mostrar_nomes(lista_nomes)
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"{nome_remover} foi removido com sucesso.")
    else:
        print(f"O nome {nome_remover} não foi encontrado.")

# Função para atualizar.
def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return

    mostrar_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}.")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")


# Mostrando menu.
while True:
    print("""
    - Gerenciador de nomes -
    1 - Adicionar
    2 - Listar nomes
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_nome(lista_nomes)
        case 2:
            mostrar_nomes(lista_nomes)
        case 3:
            atualizar_nome(lista_nomes)
        case 4:
            excluir_nome(lista_nomes)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    time.sleep(5)
    os.system("cls || clear")