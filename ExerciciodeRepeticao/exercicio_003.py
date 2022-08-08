#Faça um programa que leia e valide as seguintes informações:
#A) Nome: maior que 3 caracteres;
#B) Idade: entre 0 e 150;
#C) Salário: maior que zero;
#D) Sexo: 'f' ou 'm';
#E) Estado Civil: 's', 'c', 'v', 'd';#

nome = input("Informe seu nome:  ")
idade = int(input("Informe um número entre 0 e 150: "))
salario = int(input("Informe o seu salário: "))
sexo = input("Informe o sexo: ")
estado_civil = input("Informe o estado cívil: ")

while len(nome) <= 3:
    nome = input("Informe o nome novamente: ")
while (idade > 0) and (idade > 150):
    idade = int(input("Informe sua idade novamente: "))
while salario < 0:
    salario = int(input("Informe o salário novamente: "))
while (sexo !='f') and (sexo !='m'):
    sexo = input("Infome o sexo novamente: ")
while (estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'):
    estado_civil = input("Informe o sexo novamente: ")