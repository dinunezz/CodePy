# CONDICIONAIS IF ELSE

###########################
# Analisador de Idade
tempo = (int(input('Quantos anos vc tem? ')))
if tempo <= 25:
    print('Jovem')
else:
    print('Semivelho!')
print('Obr. por participar!')
# Forma Simplificada
print('>>> Jovem <<<' if tempo <= 25 else '>>> Semivelho <<<')

########################
# Jogo de adivinhar número
import random
print('*' * 40)
pc = random.randint(1,10)
numb = (int(input('Em qual número entre 0 e 10 eu pensei? ')))
print('Acertou!' if pc == numb else 'Errou! Pensei no {}.'.format(pc))

########################
# Analisa velocidade e calcula valor da multa
print('*' * 40)
vlc = (int(input('Informe a velocidade: ')))
if vlc <= 80:
    print('Velocidade Permitida!')
else:
    paga = (vlc - 80) * 7
    print('Acima da velocidade permitida! Multa: R${},00.'.format(paga))
print('Respeite a Sinalização!')

#########################
# Par ou Impar
print('*' * 40)
num = (int(input('Digite um número inteiro: ')))
print('{} é Par!'.format(num) if (num % 2) == 0 else '{} é Impar!'.format(num))

#########################
# Analisador de Ano Bissexto

from datetime import date

txt = (str('Que ano gostaria de analisar? Pressione 0 para o ano atual: '))
contChar = (len(txt)) # Conta qtde da caracteres da variável txt
print('*' * contChar) # Printa * na linha de acordo com a contChar
ano = (int(input(txt)))


# Se ano IGUAL a 0, ano recebe o ANO atual
if ano == 0:
    ano = date.today().year

# (if ano % 4 == 0)     SE O RESTO DA DIVISÃO DE ano POR 4 FOR == 0
# (and ano % 100)       E o RESTO DA DIVISÃO DE ano POR 100 FOR != 0
# (or ano % 400 == 0)   OU RESTO DA DIVISÃO DE ano por 400 FOR == 0

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é Ano BISSEXTO!'.format(ano))
else:
    print('{} Não é ano BISSEXTO!'.format(ano))
print('*' * contChar)
print('')

#########################

# Maior e Menor número
n1 = float(input('Digite o 1o valor: '))
n2 = float(input('Digite o 2o valor: '))
n3 = float(input('Digite o 3o valor: '))
lst = [n1, n2, n3]
order = sorted(lst)
print('O menor é {} e o maior é {}.'.format(order[0], order[2]))
print('')

##########################################################################################

# CLASSIFICAÇÃO DE ATLETAS POR IDADE

from datetime import date

print('\33[30m-=' * 28)
print('Classificação de Atletas Por Categoria')
print('\33[30m-=' * 28)

nasc = (int(input('\33[30mInforme o ano de nascimento: ')))

anoAtual = date.today().year
anoRes = anoAtual - nasc

if anoRes <= 10:
    print('Desculpe mas com {} anos de idade não pode competir!'.format(anoRes))
elif anoRes <= 15:
    print("O atleta tem {} anos de idade. \33[1;44mClassificação: Mirim\33[m".format(anoRes))
elif anoRes <= 20:
    print("O atleta tem {} anos de idade. \33[1;44mClassificação: Juvenil\33[m".format(anoRes))
else:
    print("O atleta tem {} anos de idade. \33[1;44mClassificação: Adulto\33[m".format(anoRes))

print('\33[30m-=' * 28)
