import os
os.system("clear")

contador = 0
soma_geral = 0
soma_pares = 0
par = 0
impar =0

while True:
    numero = int(input("Informe um número: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        par += 1
        soma_pares = numero
    else:
        impar += 1
    
    contador += 1
    soma_geral += numero

media_geral = soma_geral / contador
media_par = soma_pares / par

print('\nResultado do Exercício.')
print(f'\nQuantidade de pares: {par}')
print(f'Quantidade de impares: {impar}')
print(f'\nMédia pares: {media_par:.1f}')
print(f'Média geral: {media_geral:.1f}')


    
