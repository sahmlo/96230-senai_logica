import os
os.system("clear")

preco = float(input("Informe o valor do produto: "))

def inflacao (preco):
    if preco >= 100:
        valor_inflacao = preco * 1.2
        return valor_inflacao
    
    elif preco < 100:
        valor_inflacao = preco * 1.1
        return valor_inflacao 
       
def desconto (preco):
    if preco >= 100:
        valor_desconto = preco * 0.1
        return valor_desconto
        
    elif preco < 100:
        valor_desconto = preco * 0.2
        return valor_desconto    
    
preco_desconto = desconto(preco)
preco_inflacao = inflacao(preco)
print(f"O preço com inflação é: R$ {preco_inflacao:.0f}  ")
print(f"O preço com desconto é: R$ {preco_desconto:.0f}  ")