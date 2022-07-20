# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


def lata1():
    tamanho_da_area = int(input("Tamanho da área em metros: "))
    litros = int(tamanho_da_area / 6)
    valor_da_lata = int(80)
    capacidade = int(18)

    latas = int(litros / capacidade)
    
    total = latas * valor_da_lata
    print("Você usará", latas, " latas de tintas")
    print("O preço total é de R$", total)

#lata1()

def lata2():
    tamanho_da_area2 = int(input("Tamanho da área em metros: "))
    litros2 = int(tamanho_da_area2 / 6)
    valor_da_lata2 = int(25)
    capacidade2 = float(3.6)

    latas2 = int(litros2 / capacidade2)
    total2 = latas2 * valor_da_lata2
    print("Vcoê usará", latas2,"latas de tinta")
    print("O preço total é de R$", total2)                          

lata2()