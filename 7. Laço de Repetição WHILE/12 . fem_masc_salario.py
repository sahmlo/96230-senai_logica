import os 
os.system("clear")
import time

idade = 0
quantidade_woman = 0 
soma_money = 0
total_guys = 0
max_idade = 0
min_idade = 120

while True:
    print("""
Código | Descrição 
1 \t Adicionar Pessoa
2 \t Exibir Resultado
3 \t Sair
""")
    opcao = int(input("Digite a opção desejada: "))                   
    
    match opcao:
        case 1:
        
            idade = int(input("Digite sua idade: "))
            genero = (input("""                 
M - Masculino
F - Feminino
Digite seu gênero:                    
""")).upper()
            salario = float(input("Digite o valor do seu sálario: "))
            total_guys += 1
            soma_money += salario
            if genero == "F" and salario >= 5.000:
                quantidade_woman += 1
            if idade > max_idade:
                max_idade = idade

            if idade < min_idade:
                min_idade = idade   
            os.system("clear")    
        case 2:
            if total_guys > 0:
               
                print(f"\nMédia salarial do grupo: R$ {soma_money / total_guys:.3f}")
                print(f"Maior idade do grupo: {max_idade}")
                print(f"Menor idade do grupo: {min_idade}")
                print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_woman}")
            else:
                print("\nCadastre uma pessoa primeiro.")  
            time.sleep(3)
            os.system("clear")
        case 3:
            print("Encerrando o programa")
            break
        case _:
            print("Opção Inválida. Tente Novamente.")          