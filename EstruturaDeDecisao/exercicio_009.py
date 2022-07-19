# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe um número: "))
numero3 = int(input("Informe um número: "))

#print (numero1, "-", numero2, "-", numero3)


if numero1 < numero2 < numero3:
    print(numero3, "-", numero2, "-", numero1)
elif numero1 > numero2 > numero3:
    print(numero1, "-", numero2, "-", numero3)
elif numero2 > numero1 > numero3:
    print(numero2, "-", numero1, "-", numero3)

