#14.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
# João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


def papo_de_pescador():
    regulamento = 50
    peso_peixe = float(input("Insira o peso do peixe :"))
    if peso_peixe > regulamento:
        excesso = peso_peixe - regulamento
        multa = excesso * 4.00
        print("Multa foi de ", multa,"reais")
papo_de_pescador()