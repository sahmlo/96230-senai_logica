import os
os.system("clear")

peso = float(input("Informe seu peso em KG: "))
altura = float(input("Informe sua altura: "))

def altura_peso(peso,altura):
    calculo_peso_altura = peso / (altura ** 2)
    return calculo_peso_altura

def imc (calculo_peso_altura):
    if calculo_peso_altura < 18.5:
        return "Abaixo do peso, consulte um nutricionista."
    elif 18.5 <= calculo_peso_altura <= 24.9: 
        return "Peso normal, mantenha hábitos saudáveis."
    elif 25 <= calculo_peso_altura <= 29.9: 
        return "Sobrepeso, considere uma dieta balanceada e atividade física."
    elif 30 <= calculo_peso_altura <= 34.9:  
        return "Obesidade Grau 1, procure orientação de um profissional de saúde."
    elif 35 <= calculo_peso_altura <= 39.9:
        return "Obesidade Grau 2, consulte um médico para avaliação e orientação."
    elif calculo_peso_altura >= 40: 
        return "Obesidade Grau 3, busque assistência médica imediatamente."
    else:
        "Erro! Calcule novamente o IMC"

resultado = altura_peso (peso,altura)
classificacao = imc (resultado)

print(f"Seu IMC é: {resultado:.2f}")
print(f"{classificacao}")