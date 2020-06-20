# Classe
from time import sleep
class Computador:
    def __init__(self, marca, mem_ram, proc):
        self.marca = marca
        self.mem_ram = mem_ram
        self.proc = proc


# Métodos da Classe
    def ligar(self):
        from time import sleep
        print("Inicializando Sistema Operacional", end='')
        for cont in range(1, 4):
            sleep(2)
            print('.', end='')
        print()
        sleep(1)


    def desligar(self):
        print('Salvando Configurações', end='')
        for cont in range(1,4):
            sleep(1)
            print('.', end='')
        print()
        sleep(1)

        print('Encerrando Sistema Operacional', end='')
        for cont in range(1,4):
            print('.', end='')
            sleep(1)
        print()


    def informacoes_hardware(self):
        import colorize
        print(f'{colorize.color("LtVerm")}{"-=" * 15}{colorize.color("limpa")}')
        print('Configuração Do Computador:')
        print(f'Marca: {self.marca}\nMemória: {self.mem_ram}\nProcessador: {self.proc}')
        print(f'{colorize.color("LtVerm")}{"-=" * 15}{colorize.color("limpa")}')
        sleep(3)

# Instanciando Classes
# Primeiro Objeto
computador1 = Computador('Lenovo', '8GB', 'i7')
computador1.ligar()
computador1.informacoes_hardware()
computador1.desligar()
print()
print()
print()

# Segundo Objeto
computador2 = Computador('Asus', '16GB', 'i9')
computador2.ligar()
computador2.informacoes_hardware()
computador2.desligar()

