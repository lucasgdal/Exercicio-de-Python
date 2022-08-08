# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

popA = int(input("Informe a população do país A: "))
while popA < 0:
    popA = int(input("População deve ser maior que 0, digite novamente: "))

taxa_a = float(input("Informe a taxa de crescimento: "))

popB = int(input("Informe a população do país B: "))
while popB < 0:
    popB = int(input("População deve ser maior que 0, digite novamente: "))

taxa_b = float(input("Informe a taxa de crescimento: "))

ano = 2022

while popA < popB:
    ano += 1
    popA = int((1 + (taxa_a/100)) * popA)
    popB = int((1 + (taxa_b/100)) * popB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)
