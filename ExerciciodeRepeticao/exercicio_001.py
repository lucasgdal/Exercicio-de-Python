# Faça um programa que peça uma nota, entre zero e dez.
# #Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

x = int(input("Informe um número entr 0 e 10: "))

while x <= 0 or x >= 10:
    print("Número inválido")
    x = int(input("Digite novamente um número entre 0 e 10: "))

else:
    print("Número ok")
