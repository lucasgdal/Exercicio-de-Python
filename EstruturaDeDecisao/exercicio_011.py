# 11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
# contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# A) salários até R$ 280,00 (incluindo) : aumento de 20%
# B)salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# C)salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# D)salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# E)o salário antes do reajuste;
# F)o percentual de aumento aplicado;
# G)o valor do aumento;
# H)o novo salário, após o aumento.

salario_bruto = float(input("Informe seu salário bruto: "))

if salario_bruto <= 280.0:
    reajuste = float((20 / 100 + 1) * salario_bruto)
    valor_do_aumento = (salario_bruto * 0.02) * 10
    print("O salário antes do reajuste:  R$", salario_bruto, "\n"
          "Houve um aumento de 20% no salário \n"
          "O valor do aumento foi de R$", valor_do_aumento, "reais \n"
          "O novo salário é de: R$ ", reajuste, "reais")
elif 280.0 <= salario_bruto <= 700.0:
    reajuste = ((15 / 100 + 1) * salario_bruto)
    valor_do_aumento = (salario_bruto * 0.15) * 1
    print("O salário antes do reajuste:  R$", salario_bruto, "\n"
          "Houve um aumento de 15% no salário \n"
          "O valor do aumento foi de R$", valor_do_aumento, "reais \n"
          "O novo salário é de: R$ ", reajuste, "reais")

elif 700.0 <= salario_bruto <= 1500.0:
    reajuste = ((10 / 100 + 1) * salario_bruto)
    valor_do_aumento = (salario_bruto * 0.1) * 1
    print("O salário antes do reajuste:  R$", salario_bruto, "\n"
          "Houve um aumento de 10% no salário \n"
          "O valor do aumento foi de R$", valor_do_aumento, "reais \n"
          "O novo salário é de: R$ ", reajuste, "reais")

elif salario_bruto >= 1500.0:
    reajuste = ((5 / 100 + 1) * salario_bruto)
    valor_do_aumento = (salario_bruto * 0.05)
    print("O salário antes do reajuste:  R$", salario_bruto, "\n"
          "Houve um aumento de 5% no salário \n"
          "O valor do aumento foi de R$", valor_do_aumento, "reais \n"
          "O novo salário é de: R$ ", reajuste, "reais")
