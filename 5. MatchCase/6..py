import os
os.system("clear")

#Entrada
valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""Digite a forma de pagamento: 
1 - A Vista
2 - A prazo
                               """))
                         
#Solicitando dados

match forma_de_pagamento:
    case 1:
    #Aplicando desconto de 10%
        desconto = valor_produto * 0.10


    
    
#Saída