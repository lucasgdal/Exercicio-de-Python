#11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A) o produto do dobro do primeiro com metade do segundo .
#B) a soma do triplo do primeiro com o terceiro.
#C) o terceiro elevado ao cubo.

def produtos_e_inteiros():
    inteiroA = int(input("Informe um número inteiro: "))
    inteiroB = int(input("Informe um número inteiro: "))
    real = int(input("Informe um número real: "))
    resultadoA = (inteiroA * 2) + (inteiroB / 2)
    resultadoB = inteiroA * 3 + real
    resultadoC = real ** 3

    print(resultadoA)
    print(resultadoB)
    print(resultadoC)

produtos_e_inteiros()
