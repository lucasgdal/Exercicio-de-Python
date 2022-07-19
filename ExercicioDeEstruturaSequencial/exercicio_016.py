#16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def loja_de_tinta():
    tamanho_da_area = int(input("Tamanho da área em metros: "))
    litros = int(tamanho_da_area / 3)
    valor_da_lata = int(80)
    capacidade = int(18)

    latas = int(litros / capacidade)
    total = latas * valor_da_lata
    print("Você usará", latas, "latas de tintas")
    print("O preço total é de R$", total)

loja_de_tinta()