# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

entrada1 = int(input("Informe um número: "))
entrada2 = int(input("Informe um número: "))
entrada3 = int(input("Informe um número: "))

maior = entrada1
menor_entrada = entrada1

if entrada2 > maior:
    maior = entrada2
if entrada2 < menor_entrada:
    menor_entrada = entrada2
if entrada3 > maior:
    maior = entrada3

if entrada3 < menor_entrada:
    menor_entrada = entrada3

print('Maior: ', maior)
print('Menor: ', menor_entrada)
