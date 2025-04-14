import os
os.system("clear")

produto = float(input('Informe o valor do produto: '))
forma_de_pagamento = int(input('\nInforme a forma de pagamennto. \n1 - à vista. \n2 - à prazo. \nInfome a opção escolhida: '))

match forma_de_pagamento:
    case 1:
        desconto = produto - (forma_de_pagamento*0.10)
        print(f'Valor Aplicado.\nValor atualizado é: R$ {desconto:.2f}.')
        
    case 2:
        quantidade = int(input("Informe a quantidade de parcelas: "))
        if quantidade >= 1 and quantidade <= 6:
            valor_parcela = produto / quantidade

            print(f"\nValor do produto: R$ {produto} \nForma de pagamento à prazo. \nQuantidade de parcela {quantidade} \nValor por parcela: R$ {valor_parcela:.2f} \nTotal à prazo: {produto}")

        else:
            print("O parcelamento deve ser até 6 parcelas.")

    case _:
        print("Opção Invalida.")