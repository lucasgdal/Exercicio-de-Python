# Faça um programa que leia 5 números e informe o maior número.

numero = []

for i in range(1, 6):
    numero.append(int(input("Infome um núemro: ")))

maior_numero = numero[0]

cont = 1

while cont < len(numero):
    if numero[cont] > maior_numero:
        maior_numero = numero[cont]
        cont = cont + 1

print(maior_numero)
