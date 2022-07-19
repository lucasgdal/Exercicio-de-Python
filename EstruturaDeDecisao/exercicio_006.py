# 6. Faça um Programa que leia três números e mostre o maior deles.

entrada1 = int(input("Informe um número: "))
entrada2 = int(input("Informe um número: "))
entrada3 = int(input("Informe um número: "))

maior = entrada1

if entrada2 > maior:
    maior = entrada2
if entrada3 > maior:
    maior = entrada3

print('Maior: ', maior)
