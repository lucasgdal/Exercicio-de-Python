import random


jogador2 = random.choice(['pedra', 'papel', 'tesoura'])
tentativa = 3
#jogador2 = input('Insira sua arma: ')

for i in range(1, tentativa + 1):
    jogador1 = input("Insira sua arma: ")

    if jogador1 == 'papel' != jogador2 == 'pedra':
        print('Você ganhou')
        break
    elif jogador1 == 'pedra' != jogador2 == 'tesoura':
        print('Você ganhou!')
        break
    elif jogador1 == 'tesoura' > jogador2 == 'papel':
        print('Você ganhou!')
        break
    elif jogador1 == jogador2:
        print('Empate!')
    else:
        print('Você perdeu!')