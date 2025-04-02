import os 
os.system("clear")
import time

salario = 0
soma_salarios = 0
familia = 0 
numero_filhos = 0 
filhos = 0
max_salario = 0
min_salario = 24000000

while True:
    print("""
Código | Descrição 
1 \t Adicionar Pessoa
2 \t Sair e Exibir Resultado

""")
    opcao = int(input("Digite a opção desejada: "))  
    match opcao:
        case 1:
            salario = float(input("Digite o valor do seu sálario: "))
            filhos = int(input("Digite a quantidade de filhos: ")) 
            familia += 1
            soma_salarios += salario
            numero_filhos += filhos
            
            if salario > max_salario:
                max_salario = salario
            if salario < min_salario:
                min_salario = salario
        case 2:     
            if familia > 0:
                print(f"\nExibindo resultados")
                print(f"Total de familias: {familia}")
                print(f"Média de salários: R$ {soma_salarios / familia:.3f}")
                print(f"Média de filhos: {numero_filhos / familia:.0f}")
                print(f"Maior salário: {max_salario:.3f}")
                print(f"Menor salário: {min_salario:.2f}")
                print(f"\nPrograma encerrado")
            elif familia == 0:
                print("Cadastre um pessoa primeiro.")
            time.sleep(3)
            os.system("clear")
            break
        case _:
            print("Opção Inválida. Tente Novamente")
            time.sleep(3)
            os.system("clear")

 
    