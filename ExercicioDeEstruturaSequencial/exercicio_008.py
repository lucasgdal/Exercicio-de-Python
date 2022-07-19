#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

def calculo_salario():
    valor_da_hora = float(input("Insira o valor ganho por horas trabalhadas: "))
    horas_trabalhadas = float(input("Insira as horas trabalhadas: "))
    salario_mes = (valor_da_hora * horas_trabalhadas) * 24
    print("O seu salário é de R$",salario_mes)

calculo_salario()
