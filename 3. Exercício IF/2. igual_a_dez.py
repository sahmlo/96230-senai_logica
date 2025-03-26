import os
os.system("clear")

#Elabore um algorismo para solitar ao usuário um valor, escreva a mensagem: É MAIOR QUE 10!
#Se o valor lido for maior que 10,caso contrário escrever:NÃO É MAIOR QUE 10!
#verifique se o número digitado é igual a 10, caso seja, escreva a mensagem: "O número é igual a 10"

#Var:

numero = int

#Solitando dados

numero = int(input("Digite um número: "))
print(f"Número: {numero}")

#Estrutura Aninhada

if numero < 10:
    print ("NÃO É MAIOR QUE 10!")
elif numero ==  10:
    print ("É IGUAL A 10!")
else:
    print("É MAIOR QUE 10!")

print("== FIM ==")