#13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#A) Para homens: (72.7*h) - 58
#B) Para mulheres: (62.1*h) - 44.7

def peso_ideal_2():
    altura_homem = float(input("Insira sua altura: "))
    altura_mulher = float(input("Insira sua altura: "))
    peso_homem = float((72.7 * altura_homem) - 58)
    peso_mulher = float((62.1 * altura_mulher) - 44.7)
    print("O peso do homem é ",peso_homem,"quilos")
    print("O peso da mulher é ",peso_mulher,"quilos")

peso_ideal_2()