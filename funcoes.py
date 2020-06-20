# FUNÇÕES

import banner
from random import randint
from time import sleep

# DICIONARIO DE CORES
cores = {"limpa": "\033[m",
         "FundoBranco": "\033[40m",
         "FundoVerde": "\033[42m",
         "FundoAzul": "\033[44m",
         "LetraBranco": "\033[30m",
         "LetraVerde": "\033[1;32m",
         "LetraAzul": "\033[34m",
         "BrancaFverm": "\33[1;30;41m",
         "VermFBranco": "\33[1;31;40m",
         "LetraVerm": "\033[31m",
         }


###################################################
'''
# USANDO LISTA NAS FUNÇÔES
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

import banner
banner.topo(" *** USANDO LISTA NAS FUNÇÔES *** ")

vlres = [2, 4, 6, 8]
print(vlres)
dobra(vlres)
print(vlres)
print()

#'''
###################################################
'''
# USANDO FUNÇÔES DENTRO DE FUNÇÔES E EMPACOTANDO VALORES DE PARAMETRO
from random import randint


def soma(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'Foram {len(valores)} números informados cuja soma é {s}.')


banner.topo(" *** FUNÇÔES DENTRO DE FUNÇÔES E EMPACOTANDO VALORES DE PARAMETRO *** ")
soma(2, 4)
soma(9, 10, 12, 17, 7)
soma(9, 10, 12, 17, 7, 9, 10, 12, 17, 7, 9, 10, 12, 1)
soma(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100),
     randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100),
     randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100),
     randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print()

'''
###################################################
#'''
def area(l, c):
    """
    Calcula Area de Terreno.
    Feito Por Diego Nunes em Maio 2020
    """
    t = l * c
    print(f'Area do Terreno {l} X {c} é {t} M2')

banner.topo(" *** Função Calcula Área *** ")
l = float(input('Informe a largura do terreno em metros: '))
c = float(input('Informe o comprimento do terreno em metros: '))
area(l, c)
print()
'''
###################################################
'''
def soma(a, b):
    """
    :param a:
    :param b:
    :return:
    """

    s = a + b
    return s

banner.topo(' *** FUNÇÃO SOMA + RETURN *** ')
r = soma(7, 7)
if r % 2 == 0:
    print('O retorno da função é Par!')
else:
    print('O Retorno da função é Ímpar')
print(r)
print()

'''
###################################################
'''
def sorteia(lista):
    """
    :param lista:
    :return:
    """
    print('Soteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('OK!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando valores pares de {lista}, temos {soma}')


banner.topo(" *** FUNÇÃO SORTEIA NÚMEROS E SOMA OS PARES *** ")
numeros = list()
sorteia(numeros)
somaPar(numeros)
print()

'''
##################################################
'''
# MINHA SOLUÇÃO
def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade > 18 and idade < 65:
        print(f'Com {idade} o voto é obrigatório!')
    else:
        print(f'Com {idade} o voto é opcional!')


banner.topo(" *** FUNÇÃO CALCULA VOTO *** ")
voto(1985)
print()

# SOLUÇÂO DO PROF
def votoProf(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


banner.topo(" *** FUNÇÃO CALCULA VOTO - SOLUÇÃO DO PROF *** ")
nasc = int(input('Ano de Nascimento: '))
print(votoProf(nasc))
print()

'''
##################################################
'''
def fatorial(n, show=False):
    """
    CALCULA O FATORIAL DE UM NÚMERO INFORMADO
    :param n: número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O Valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Main
banner.topo(" *** CALCULA FATORIAL *** ")
print(fatorial(5, show=True))
print()
help(fatorial)
print()

'''
##################################################
'''
# CRIANDO FUNÇÃO PARA LER SOMENTE NÚMEROS INTEIROS
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cores["LetraVerm"]}ERRO! Digite um número válido.{cores["limpa"]}')
        if ok:
            break
    return valor


#Main
banner.topo(" *** CRIANDO FUNÇÃO PARA LER SOMENTE NÚMEROS INTEIROS *** ")
n = leiaInt('Digite um número: ')
print(f'{cores["VermFBranco"]}Número digitado: {n}{cores["limpa"]}')
print()

'''
##################################################
'''
# FUNÇÃO RECEBE VALORES E JOGA EM UM DICIONARIO
def notas(*n, sit=False):
    """
    ANALISA NOTAS E SITUAÇÃO DO ALUNO
    :param n: notas informadas (uma ou mais)
    :param sit: valor bool opcional para informar situação do aluno
    :return: dicionário com as informações passadas: Boa, Razoável ou Ruim
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Main
banner.topo(" *** FUNÇÃO RECEBE VALORES E JOGA EM UM DICIONARIO *** ")
resp = notas(5, 7, 10, 6, sit=True)
print(resp)

'''
##################################################
#'''
# CONTA DIAS RESTANTES PARA ANIVERSÁRIO
def ContaDias():
    from datetime import date
    dtHoje = date.today()
    dtNiver = date(2020, 8, 4)
    d = dtNiver - dtHoje
    print(f'Falta(m) {d.days} dias para quem anivérsária em {dtNiver}')


ContaDias()
