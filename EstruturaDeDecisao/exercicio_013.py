# 13. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nome_do_aluno = input("Informe seu nome: ")
nota1 = float(input("Informe sua nota do primeiro bimestre: "))
nota2 = float(input("Informe sua nota do segundo bimestre: "))
media_do_aluno = (nota1 + nota2) / 2

if 9.0 <= media_do_aluno <= 10.0:
    print("Nome: ", nome_do_aluno, "\n"
      "Nota do 1ºBimestre: ", nota1, "\n"
      "Nota do 2ºBimestre: ", nota2, "\n"
      "Média do aluno: ", media_do_aluno, "\n"
      "Conceito do Aluno: A" "\n" )
elif 7.5 <= media_do_aluno <= 9.0:
    print("Nome: ", nome_do_aluno, "\n"
      "Nota do 1ºBimestre: ", nota1, "\n"
      "Nota do 2ºBimestre: ", nota2, "\n"
      "Média do aluno: ", media_do_aluno, "\n"
      "Conceito do Aluno: B" "\n" "Status: APROVADO")
elif 6.0 <= media_do_aluno <= 7.5:
    print("Nome: ", nome_do_aluno, "\n"
      "Nota do 1ºBimestre: ", nota1, "\n"
      "Nota do 2ºBimestre: ", nota2, "\n"
      "Média do aluno: ", media_do_aluno, "\n"
      "Conceito do Aluno: C" "\n" "Status: APROVADO")
elif 4.0 <= media_do_aluno <= 6.0:
    print("Nome: ", nome_do_aluno, "\n"
      "Nota do 1ºBimestre: ", nota1, "\n"
      "Nota do 2ºBimestre: ", nota2, "\n"
      "Média do aluno: ", media_do_aluno, "\n"
      "Conceito do Aluno: D" "\n" "Status: REPROVADO")
elif 0 <= media_do_aluno <= 4.0:
    print("Nome: ", nome_do_aluno, "\n"
      "Nota do 1ºBimestre: ", nota1, "\n"
      "Nota do 2ºBimestre: ", nota2, "\n"
      "Média do aluno: ", media_do_aluno, "\n"
      "Conceito do Aluno: E" "\n" "Status: REPROVADO")