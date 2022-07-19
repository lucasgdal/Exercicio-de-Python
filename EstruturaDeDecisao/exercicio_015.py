# 15. Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

ladoA = int(input("Infome o lado: "))
ladoB = int(input("Infome o lado: "))
ladoC = int(input("Infome o lado: "))

if (ladoA + ladoB < ladoC) or (ladoA + ladoC < ladoB) or (ladoB + ladoC < ladoA):
    print("Não é um triângulo")
elif (ladoA == ladoB) and (ladoA == ladoC):
    print("Triângulo Equilátero")

if (ladoA == ladoB) and ladoC == ladoB or ladoA == ladoC:
    print("Triângulo Isósceles")

if ladoA != ladoB != ladoC:
    print("Triâgulo Escaleno")
