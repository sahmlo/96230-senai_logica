import os
os.system ("clear")

#Elabore um algorismo usando operações lógicas para solicitar ao usuario 2 números e escrever :
#Os dois números informados
#O maior número
#O menor número

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

menor = min (primeiro_numero, segundo_numero)
maior = max (primeiro_numero, segundo_numero)

#print ("\nExibindo Dados: ")
#print (f"MAIOR: {maior}")
#print (f"MENOR: {menor}")


if primeiro_numero == segundo_numero: 
    print ("Os números são igauis.")
else:
    print (f"Primeiro número {primeiro_numero}")
    print (f"Segundo número {segundo_numero}")
    print (f"MAIOR: {maior}")
    print (f"MENOR: {menor}")