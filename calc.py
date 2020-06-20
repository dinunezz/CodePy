# Sem Uso de Muitas Variaveis
print('>>> Primeira Execução:')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('soma: ', n1 + n2)
print('Subtração: ', n1 - n2)
print('multiplicação: ', n1 * n2)
print('Divisão: ', n1 / n2)
print('')
print('')

# Com Uso de Muitas Variaveis
print('>>> Segunda Execução:')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
resDiv = n1 % n2
pot = n1 ** n2
print(' Soma: {}, \n Subtração: {}, \n Multiplicação: {}, \n Divisão: {}, \n Divisão Inteira: {},'
      ' \n Resto da Divisão: {},\n Potência: {}'.format(soma,sub,mult,div,divInt,resDiv,pot))
print('')
print('')

#####################################################################################################

# Mostra Num Antecessor, Sucessor e Raiz Quad
num = int(input('Informe um número: '))
print('Seu ANTECESSOR é {} e seu SUCESSOR é {}'.format((num - 1), (num + 1)))
print('Seu Dobro é {}'.format(num ** 2))
print('Seu Triplo é: {} '.format(num ** 3))
print('Sua Raiz Quadrada é: {:.2f}'.format(num ** (1/2)))
print('')
print('')

########################################################################################################

# Tabuada
print('-' * 20)
n = int(input('Digite um número para saber a tabuada: '))
print('-' * 20)
print('A tabuada de {}'.format(n))
print('{} X 1 = {}'.format(n, n*1))
print('{} X 2 = {}'.format(n, n*2))
print('{} X 3 = {}'.format(n, n*3))
print('{} X 4 = {}'.format(n, n*4))
print('{} X 5 = {}'.format(n, n*5))
print('{} X 6 = {}'.format(n, n*6))
print('{} X 7 = {}'.format(n, n*7))
print('{} X 8 = {}'.format(n, n*8))
print('{} X 9 = {}'.format(n, n*9))
print('{} X 10 = {}'.format(n, n*10))
print('-' * 20)
print('')
print('')
########################################################################################################

# Calc Compra de Dolares
real = int(input('Informe qto vc tem na carteira? R$'))
dlr = real / 3.27
print('Com R${:.2f} da para comprar US${:.2f}'.format(real, dlr))
print('')
print('')

########################################################################################################

# Calc Qtde de Tinta
alt = float(input('Informe a altura da parede que deseja pintar: '))
larg = float(input('Agora informe a largura: '))
area = alt * larg
qtd = area / 2
print('Para pintar a parede de {} M2, gasta {} Litros de tinta.'.format(area, qtd))
print('')
print('')

########################################################################################################

# Calc Desconto porcento
prc = float(input('Digite o preço do produto: R$'))
desc = int(input('Informe o desconto: '))
novoprc = prc - (prc * desc / 100)
print('Com desconto de {}% o valor do produto será R${:.2f}'.format(desc,novoprc))
print('')
print('')

########################################################################################################

# Importando Módulo math para calculo de Raiz Quadrada
# Importa toda a biblioteca: math
# from math import sqrt (importa apenas a sqrt)
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))
print('')
print('')


