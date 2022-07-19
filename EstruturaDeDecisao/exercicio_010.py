# 10.Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


print(" Se você estuda no turno da manhã digite M-matutino\n "
      "Se você estuda no turno da tarde digite V-vespertino\n"
      " Se você estuda no turno da noite digite N-noturno ")

turno = input("Informe o turno que você estuda: ")

if turno == 'M-matutino':
      print("Bom dia!")
elif turno == 'V-vespertino':
      print("Boa tarde!")
elif turno == 'N-noturno':
      print("Boa noite!")
else:
      print("Valor Inválido!")

