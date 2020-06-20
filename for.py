# Usando FOR

# CONTAGEM REGRESSIVA
from time import sleep
for c in range (10,0,-1):
    print('Contagem Regressiva {}'.format(c))
    sleep(1)
print('FELIZ ANO NOVO!')
print('=-' * 15)
print()

#######################################################################

# CONTAGEM DE NUMEROS PARES DE 0 A 50
for c in range (0,51,2):
    print(c)
print('Fim da Contagem!')
print()

#######################################################################

# Soma de números impares e multiplos de 3 entre 1 e 500
soma = 0
cont = 0
for c in range(1,501,2):
    if (c % 3) == 0:
        cont = cont + 1
        soma = (soma + c)
print('Resultado dos {} valores somados é: {}'.format(cont, soma))
print('=-' * 15)
print()

#######################################################################

# Tabuada Com For
mult = int(input('Quer ver a tabuada de qual número: '))
for c in range(1,11):
    print('{} X {} = {}'.format(mult,c,(mult*c)))
print()

#######################################################################

# Soma de 6 numeros apenas se for PAR
print('=-' * 15)
print('SOMA DE NÚMEROS PARES')
print('=-' * 15)
num = 0
soma = 0
for c in range(1,7):
    num = int(input('Digite o {}o número: '.format(c)))
    if (num % 2) == 0:
        soma = soma + num

if (soma != 0):
    print('A soma dos números pares é {}'.format(soma))
else:
    print('Não há números Pares para somar!')
print('=-' * 15)
print()

#######################################################################
# PALINDROMO COM FOR
frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inv = junto[::-1] # LENDO A VARIAVEL DE TRAS PRA FRENTE
#for letra in range(len(junto) -1, -1, -1): # LENDO A VARIAVEL DE TRAS PRA FRENTE COM FOR
#   inv += junto[letra]
print(junto, inv)

