#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Informe o preço do produto: "))
produto2 = float(input("Informe o preço do produto: "))
produto3 = float(input("Informe o preço do produto: "))

menor = produto1

if produto1 < menor:
    menor = produto1
if produto2 < menor:
    menor = produto2
if produto3 < menor:
    menor = produto3

print(menor)