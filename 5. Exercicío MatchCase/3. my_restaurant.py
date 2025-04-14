import os
os.system ("clear")


opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 40,00
2 \t Lasanha \t\t R$ 30,00
3 \t Strognoff \t\t R$ 20,00
4 \t Bife Acebolado \t R$ 30,00
5 \t Pão com ovo \t\t R$ 10,00
                  
Dígite a opção desejada:                  
                                   
"""))

#PROCESSAMENTO
match opcao:
    case 1:
        print("Picanha R$ 40,00")
    case 2:
        print("Lasanha R$ 30,00")
    case 3:
        print("Strognoff R$ 20,00")
    case 4:
        print("Bife Acebolado R$ 30,00")
    case 5:
        print("Pão com ovo R$ 10,00")
    
    case _:
        print("Opção Inválida")
        