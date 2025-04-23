import os
os.system("clear")

soma = 0
preco = 0
pratos_escolhidos = []

def adicionar_prato(pratos_escolhidos, prato, preco, soma):
        if preco > 0:
            pratos_escolhidos.append(prato)
        soma += preco
        return pratos_escolhidos, soma
        
print("Welcome My Restaurant")
 
while True:
    opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$25,00
2 \t Lasanha \t\t R$20,00
3 \t Strogonoff \t\t R$18,00                                 
4 \t Bife Acebolado \t R$15.00
5 \t Pão com ovo \t\t R$5,00
                  
Digite a opção desejada: """))
    match opcao:
         case 1:
             prato = "Picanha"
             preco = 25
         case 2:
             prato = "Lasanha"
             preco = 20
         case 3:
             prato = "Strogonoff"
             preco = 18
         case 4:
             prato = "Bife Acebolado"
             preco = 15
         case 5:
             prato = "Pão com ovo"
             preco = 5
         case _:
             print("\nOpção Inválida")
             preco = 0
    pratos_escolhidos, soma = adicionar_prato(pratos_escolhidos, prato, preco, soma)
    
    continuar = input("Deseja informa outro prato? (S/N): ").lower()
    if continuar == "n":
        break
    os.system("clear")

print(f"\nDetalhes do pedido\n")
for i, prato in enumerate(pratos_escolhidos, 1):
    print(f"{i} - {prato}")
print(f"\nTotal: R$ {soma:.2f}")
print("Agradeçemos a preferêrencia!")