#15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#A)salário bruto.
#B)quanto pagou ao INSS.
#C)quanto pagou ao sindicato.
#D) o salário líquido.
#E) calcule os descontos e o salário líquido, conforme a tabela abaixo:

def salario_mensal():
    salario_por_hora = float(input("Insira o valor recebido por hora trabalhada: "))
    horas_trabalhadas = float(input("Insira as horas trabalhadas: "))
    salario_bruto = (salario_por_hora * horas_trabalhadas) * 30
    imposto_de_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato
    respostaA = salario_bruto
    respostaB = inss
    respostaC = sindicato
    respostaD = salario_liquido
    resultado1 = salario_bruto - imposto_de_renda
    resultado2 = resultado1 - inss
    resultado3 = resultado2 - sindicato

    #print(respostaA)
    ##print(respostaB)
    #print(respostaC)
    #print(respostaD)
    print("+ Salário Bruto : R$",salario_bruto,
    "\n- IR (11%) : R$",resultado1,
    "\n- INSS (8%) : R$",resultado2,
    "\n- Sindicato ( 5%) : R$",resultado3,
    "\n= Salário Liquido : R$",salario_liquido)



salario_mensal()