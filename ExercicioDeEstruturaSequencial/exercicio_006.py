# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def calculo_da_area():
    raio = float(input("Informe o raio do círculo: "))
    area = 3.14 * (raio**2)
    print(area)

calculo_da_area()