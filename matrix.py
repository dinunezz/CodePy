# FUNÇÃO PARA PREENCHER TELA COM BINARIOS
# ALEATÓRIOS TIPO O EFEITO MATRIX
def Matrix():
    from random import randint
    from time import sleep
    #import colorize
    while True:
        for numb in range(0, 55):
            numb = randint(0, 1)
            print(f'{numb}', end='  ')
            #print(f'{colorize.color("LtVerde")}{numb}{colorize.color("limpa")}', end='  ')
        sleep(0.3)
        print('\n')


Matrix()