# 2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

x = int(input("Favor informar um número: "))
y = int(input("Favor informar um número: "))

if x <= y or y >= x:
    print("O X é um número negativo")
    print("O y é um número positivo")
else:
    print("O X é um número positivo")
    print("O Y é um número negativo")
