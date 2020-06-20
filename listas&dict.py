# TRABALHANDO COM LISTAS & DICIONARIOS

numeros = [10,6,4,8,2,16,12,18,14]
numeros.append(20) # Adiciona no final da lista
numeros.insert(21,22) # Inserir o 22 na posição 21

print('Lista Ordenada:', end = ' ')
numeros.sort()
print(numeros)

print('Lista Reversa: ', end=' ')
numeros.sort(reverse = True)
print(numeros)

numeros.sort(reverse = False)
print('Eliminado ítem na ultima posição da lista ordenada:', end = ' ')
numeros.pop()
print(numeros)

print('Eliminado na posição [9]:', end = ' ')
numeros.pop(9)
print(numeros)

print('Eliminando número 12 com Remove:', end = ' ')
numeros.remove(12)
print(numeros)

print('Qtde de Elementos da Lista:', end = ' ')
print(len(numeros))

print('Mostrando indice e valor com for + enumerate:')
for i, v in enumerate(numeros):
    print('Ind {} Vlr {}'.format(i, v))

'''
#######################################################
'''

num = []
for i in range(0,6):
    num.append(int(input('Informe o valor da posição {} da lista: '.format(i))))
num.sort()
print('Menor é {} \nMaior é {}'.format(num[0], num[5]))

'''
#######################################################
'''

n = list()
vlr = ''
rsp = ''
while True:
    vlr = int(input('Digite um valor para guardar: '))
    if vlr in n:
        print('Valor Duplicado!')
    else:
        n.append(vlr)
        print('Valor Adicionado com sucesso!')
    rsp = (input('Deseja Continuar? [S/N] '))
    if rsp in 'Nn':
        break
n.sort()
print('Números digitados: {}'.format(n))

'''
#######################################################
'''

lista = list()
listPar = list()
listImpar = list()
t = len(lista)
while True:
    lista.append(int(input('Informe um valor para guardar na lista: ')))
    resp = str(input('Deseja Continar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        listPar.append(v)
    else:
        listImpar.append(v)

print(f'Todos os valores: {lista}')
print('Pares: {}'.format(listPar))
print('Impares: {}'.format(listImpar))

'''
#######################################################
'''
# APPEND EM LISTAS SEPARADAS DENTRO DA MESMA LISTA

num = [[], []]
for cont2 in range(1, 8):
    vlr1 = int(input(f'Digite o {cont2}o valor: '))
    if vlr1 % 2 == 0:
        num[0].append(vlr1)
    else:
        num[1].append(vlr1)
num[0].sort()
num[1].sort()
print(f'Pares: {num[0]}')
print(f'Ímpares: {num[1]}')

'''
#######################################################
'''
# CRIANDO UMA MATRIZ COM LISTAS

matriz = [[], [], []]
vlr2 = pares = somacol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        vlr2 = int(input(f'Digite valor para [{linha}, {coluna}]: '))
        matriz[linha].append(vlr2)
print()

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()
print()

print(f'Soma dos Pares: {pares}' )

for linha in range(0, 3):
    somacol += matriz[linha][2]
print(f'Soma 3a Coluna: {somacol}')
print(f'Maior da segunda linha: {max(matriz[1])}')

'''
#######################################################
'''
from random import randint
lista = []
jogos = []
print('=' * 35)
quantDesejada = int(input('Quantos Jogos Desejar Sortear: '))
print('=' * 35)
totalJogos = 1
while totalJogos <= quantDesejada:
    contaNumerosSort = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contaNumerosSort += 1
        if contaNumerosSort >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogos += 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')

'''
#######################################################
#'''
ficha = []
while True:
    nomeAluno = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nomeAluno, [nota1, nota2], media])
    r = str(input('Continuar Cadastrando? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 20)
print(f'{"No":<6}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 20)
for i, v in enumerate(ficha):
    print(f'{i:<4} {v[0]:<10} {v[2]:>8.1f}')
print('-=' * 20)


#################################################################
'''
pessoas = {'nome':'Diego',
      'idade':'34',
      'sexo':'M'
    }
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(f'Chave: {k}')

for v in pessoas.values():
    print(f'Valores Guardados: {v}')

for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
#################################################################
#'''
dicioPessoas = dict()
listaPopulacao = list()

while True:
    dicioPessoas['nome'] = str(input('Nome: '))
    dicioPessoas['idade'] = str(input('Idade: '))
    listaPopulacao.append(dicioPessoas.copy())
    r = str(input('Continuar? '))
    if r in 'Nn':
        break
for i, v in enumerate(listaPopulacao):
    print(f'{i} = {v}')

'''
#################################################################
#'''

alunos = dict()
listagem = list()
while True:
    alunos['nome'] = str(input('Informe o nome do Aluno: '))
    alunos['n1'] = float(input(f'Informe 1a nota de {alunos["nome"]}: '))
    alunos['n2'] = float(input(f'Informe 2a nota de {alunos["nome"]}: '))
    alunos['media'] = (alunos['n1'] + alunos['n2']) / 2
    if alunos['media'] > 6:
        alunos['situacao'] = 'Aprovado'
    else:
        alunos['situacao'] = 'Reprovado'
    #listagem.append(alunos.copy())
    #alunos.clear()
    r = str(input('Deseja continuar? [S/N] ')).split()[0]
    if r in 'Nn':
        break
#for c, v in enumerate(listagem):
#    print(c, v)
for k, v in alunos.items():
    print({v}, end=' ')

'''
#################################################################
#'''
# JOGO DOS DADOS

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6)}

print('  ==  Valores Sorteados Nos Dados  ==')
for k, v in jogo.items():
    print(f'      {k} tirou {v}')
    sleep(1)
print()

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('  ==  Ranking Dos Jogadores  ==')
for i, v in enumerate(ranking):
    print(f'    {i+1} Lugar: {v[0]} com {v[1]}')
    sleep(1)
'''
#################################################################
#'''
pessoa = dict()
galera = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    galera.append(pessoa.copy())
    while True:
        r = str(input('Quer Contunuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Apenas S ou N.')

    if r == 'N':
        break

print(galera)
