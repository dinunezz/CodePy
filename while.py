# REPETIÇÕES COM WHILE

cores = {'limpa':'\033[m',
         'FundoBranco':'\033[40m',
         'FundoVerde':'\033[42m',
         'FundoAzul':'\033[44m',
         'LetraBranco':'\033[30m',
         'LetraVerde':'\033[32m',
         'LetraAzul':'\033[34m'}

#################################################################################
#'''

# CONTADOR DE NÚMEROS PARES E IMPARES
n = 1
par = impar = 0
while n != 0:
    n = int(input('Informe um Número ou 0 para Sair: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foram {} Pares e {} Impares'.format(par, impar))
print()

##############################################################################
#'''

# Validando caracter informado
# Minha Solução

sex = ''
while (sex != 'M') and (sex != 'F'):
    sex = str(input('Informe Seu Sexo [M/F]: ')).upper()
print('OK!')
print()

# Solução Curso
sexo = str(input('Informe Seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválido! Informe Seu Sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso.'.format(sexo))
print()

#################################################################################
#'''

# Jogo de Adivinhar um número com While - versão 2.0

# Minha Solução:

from random import randint
rand = randint(1, 10)
jog = 0
cont = 0
while jog != rand:
    jog = int(input('Entre 1 e 10, em que número eu pensei: '))
    cont += 1
print('Parabéns! Acertou com {} tentativas.'.format(cont))
print()

# SOLUÇÃO DO CURSO

from random import randint
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou com {} tentativas.'.format(palpites))
print()

#################################################################################
#'''

# CRIANDO UMA CALC COM MENU DE OPÇÕES
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
menu = 0
sair = False
while not sair:
    print('-' * 63)
    print('[ 1 ]Somar | [ 2 ]Mutiplicar | [ 3 ]Novos Números | [ 5 ]Sair')
    print('-' * 63)
    menu = int(input('Qual a sua opção: '))
    if menu == 1:
        print('\33[34m{} + {} = {}\33[m'.format(valor1, valor2, valor1 + valor2))
    elif menu == 2:
        print('\33[34m{} x {} = {}\33[m'.format(valor1, valor2, valor1 * valor2))
    elif menu == 3:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif menu == 5:
        sair = True
    else:
        print('-' * 63)
        print('\33[34mOpção Invalida!\33[m')
print('-' * 63)
print('< Fim Do Programa >')
print()


#################################################################################
#'''

# CALCULO FATORIAL

num1 = int(input('Informe o múmero para calcular seu fatorial: '))
cont = num1
fat = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(fat)
print()


#################################################################################
#'''

# USANDO WHILE + BREAK
cont = 0
soma = 0
while True:
    vlr = int(input('Digite um valor ou 999 para parar: '))
    if vlr == 999:
        break
    soma += vlr
    cont += 1
print(f'A SOMA DOS {cont} DIGITADOS DA {soma}.')
print()


#################################################################################
#'''

# TABUADA COM WHILE E BREAK
cont = 1
while True:
    print('=' * 40)
    n = int(input('Deseja ver a tabuada de qual número: '))
    print('=' * 40)
    if n < 0:
        break
    for cont in range(1,11):
        print('{} X {} = {}'.format(n, cont, n * cont))
        cont += 1
print('>>> Fim do Programa <<<')
print()

#################################################################################
#'''

# JOGO DO PAR OU IMPAR COM WHILE
from random import randint

while True:
    micro = randint(1,10)
    print('-' * 30)
    print('*** JOGO DO PAR OU ÍMPAR ***')
    print('-' * 30)
    jogada = int(input('Qual número vc escolhe: '))
    soma = micro + jogada
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]

    if soma % 2 == 0 and tipo == 'P':
        print('{}>>>> Humano Vence <<<<{}'.format(cores['LetraVerde'], cores['limpa']))
    elif soma % 2 != 0 and tipo == 'I':
        print('{}>>>> Humano Vence <<<<{}'.format(cores['LetraVerde'], cores['limpa']))
    else:
        print('{}>>>> Máquina Vence <<<<{}'.format(cores['LetraVerde'], cores['limpa']))
        print(f'Micro: ({micro}) + Humano: ({jogada})')
        print('Total: {}'.format(micro + jogada), end=' ')
        print('Deu PAR!' if soma % 2 == 0 else 'Deu Ímpar!')
        break

    print(f'Micro: ({micro}) + Humano: ({jogada})')
    print('Total: {}'.format(micro + jogada), end=' ')
    print('Deu PAR!' if soma % 2 == 0 else 'Deu Ímpar!')

print('-' * 30)
print('FIM DE JOGO')
print('-' * 30)
print()


#################################################################################
'''

# CONTA CEDULAS EM SAQUE

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valorSaque = int(input('Quanto deseja sacar? '))
total = valorSaque
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
'''

#################################################################################

