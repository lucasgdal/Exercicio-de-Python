# 5. Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# B) A mensagem "Reprovado", se a média for menor do que sete;
# C) A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Informa a primeira nota: "))
nota2 = float(input("Informa a segunda nota: "))
media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif 7 <= media < 10:
    print("Aprovado")
else:
    print("Reprovado")
