import random
import banner

banner.topo(' *** Exemplos do Random *** ')
print(random.random()) # Valor 0.0 até 1.0
print(random.uniform(1, 5)) # Valor Decimal do min ao max
print(random.randint(1, 10)) # Valor Inteiro do min ao max

cores = ['Verde', 'Azul', 'Vermelho']
print(random.choice(cores)) # Escolhe uma opção dentro de uma lista

cartas = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(cartas) # Embaralha a ordem da lista
print(cartas)
print()


############################################################
# EXERCICIO
# Joga os valores dentro de uma lista
banner.topo('*** Informe valores para escolha de um aleatório *** ')

n1 = str(input('1o nome: '))
n2 = str(input('2o nome: '))
n3 = str(input('3o nome: '))
n4 = str(input('4o nome: '))
n5 = str(input('5o nome: '))
lst = [n1, n2, n3, n4, n5] # Joga os valores dentro de uma lista
res = random.choice(lst) # Escolhe um valor da lista
print('Escolhido: {}'.format(res))


############################################################
# Imprime caracteres na tela

while True:
    import colorize
    from time import sleep
    for cont in range(0, 55):
        a = ['@', '$', '&', '%', '§']
        b = random.choice(a)
        print(f'{colorize.color("LtVerde")}{b}{colorize.color("limpa")}', end='  ')
    print('\n')
    sleep(0.3)

