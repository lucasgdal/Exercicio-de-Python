# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# #mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = input("Insira o login: ")
senha = input("digite sua senha: ")

while senha == nome_usuario:
    print("Senha igual ao login, digite novamente")
    nome_usuario = input("Insira o login: ")
    senha = input("digite sua senha: ")
else:
    print("Dados válidados com sucesso")
