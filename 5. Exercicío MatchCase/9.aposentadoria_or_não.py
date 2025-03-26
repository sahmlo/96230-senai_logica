import os
os.system ("clear")

matricula = int(input('Informe sua matrícula: '))
ano_trabalho = int(input('Informe o tempo trabalhado: '))
ano_nascimento = int(input('Informe o ano de nascimento: '))

idade = 2025 - ano_nascimento

if idade >= 65 or ano_trabalho >= 30:
    print(f"Empregador da matrícula {matricula} \n{idade} anos\n{ano_trabalho} anos trabalhados \nRequerer Aposentadoria.")
else:
    print('Não requerer aposentadoria.')
