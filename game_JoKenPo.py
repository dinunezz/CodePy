# Game JO KEN PO

from time import sleep
from random import randint

print('-=' * 15)
print('>>> GAME JO KEN PO <<<')
print('-=' * 15)

lst = (1, 2, 3)
MicroEscolhe = randint(1, 3)

print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogadorEscolhe = (int(input('Qual a sua jogada? ')))

print('-=' * 15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 15)
if MicroEscolhe == 1: # Micro Pedra
    if jogadorEscolhe == 1: # Pedra
        print('Micro Escolhe Pedra')
        print('Jogador Escolhe Pedra')
        print('Empate!')
    elif jogadorEscolhe == 2: # Papel
        print('Micro Escolhe Pedra')
        print('Jogador Escolhe Papel')
        print('Jogador Vence!')
    elif jogadorEscolhe == 3: # Tesoura
        print('Micro Escolhe Pedra')
        print('Jogador Escolhe Tesoura')
        print('Micro Vence!')
    else:
        print('Jogada Inválida!')

if MicroEscolhe == 2: # Micro Papel

    if jogadorEscolhe == 1: # Pedra
        print('Micro Escolhe Papel')
        print('Jogador Escolhe Pedra')
        print('Micro Vence!')
    elif jogadorEscolhe == 2: # Papel
        print('Micro Escolhe Papel')
        print('Jogador Escolhe Papel')
        print('Empate!')
    elif jogadorEscolhe == 3: # Tesoura
        print('Micro Escolhe Papel')
        print('Jogador Escolhe Tesoura')
        print('Jogador Vence!')
    else:
        print('Jogada Inválida!')

if MicroEscolhe == 3: # Micro Tesoura

    if jogadorEscolhe == 1: # Pedra
        print('Micro Escolhe Tesoura')
        print('Jogador Escolhe Pedra')
        print('Jogador Vence!')
    elif jogadorEscolhe == 2: # Papel
        print('Micro Escolhe Tesoura')
        print('Jogador Escolhe Papel')
        print('Micro Vence!')
    elif jogadorEscolhe == 3: # Tesoura
        print('Micro Escolhe Tesoura')
        print('Jogador Escolhe Tesoura')
        print('Empate!')
    else:
        print('Jogada Inválida!')

print('-=' * 15)