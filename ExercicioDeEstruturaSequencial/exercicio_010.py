#10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def conversao_temperatura_celcius():
    temperatura_celcius = int(input("Informe a temperatura em Celcius: "))
    conversor = (temperatura_celcius * 9) / 5 + 32
    print("A temperatura em Fahrenheit é de ", conversor,"graus")

conversao_temperatura_celcius()