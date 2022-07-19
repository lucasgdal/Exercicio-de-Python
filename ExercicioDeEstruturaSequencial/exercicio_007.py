# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calculo_da_area_quadrado():
    base = float(input("Informe o valor da base do quadrado: "))
    altura = float(input("Informe o valor de altura do quadrado: "))
    area = (base * altura) * 2
    print("O dobro da área do quadrado é ", area, "cm")

calculo_da_area_quadrado()