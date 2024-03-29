# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. #
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou
# iguale a população do país B, mantidas as taxas de crescimento.

popA = 80000
popB = 200000
taxa_a = 3
taxa_b = 1.5

ano = 0

while popA < popB:
    ano += 1
    popA = int((1 + (taxa_a/100)) * popA)
    popB = int((1 + (taxa_b/100)) * popB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)
