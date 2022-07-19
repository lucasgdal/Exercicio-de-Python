# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media_escolar():
    nota1 = float(input("Insira sua nota: "))
    nota2 = float(input("Insira sua nota: "))
    nota3 = float(input("Insira sua nota: "))
    nota4 = float(input("Insira sua nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print("A sua média final é ", media)

media_escolar()