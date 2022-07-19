#12.Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def peso_ideal():
    altura = float(input("Informe sua altura: "))
    peso = float((72.7 * altura) - 58)
    print("O peso ideal é: ", peso)

peso_ideal()