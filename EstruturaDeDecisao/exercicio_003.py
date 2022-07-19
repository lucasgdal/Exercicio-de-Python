# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input("Informe seu gênero: ")

if genero == "M":
    print("M - Mascluino")
elif genero == "F":
    print("F - Feminino")
else:
    print("Sexo Invalido")
