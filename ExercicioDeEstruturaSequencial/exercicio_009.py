#9.Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

def conversao_temperatura_fahrenheit():
    temperatura_fahrenheit = float(input("Informa temperatura em Fahrenheit: "))
    conversor_temperatura = int(5 * ((temperatura_fahrenheit - 32) / 9 ))
    print("A temperatura em Celsius é de ",conversor_temperatura,"graus")

conversao_temperatura_fahrenheit()