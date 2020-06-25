class Programas:
    '''

    Classe Generalista que ira fornecer seus métodos e atributos para outras classes

    '''
    def __init__(self, nome, ano):
        self._nome = nome.title()  # __nome: torna o atributo (nome) privado
        self.ano = ano
        self._likes = 0

    # Encapsulamento
    @property
    def like(self):
        return self._likes  # Acessa o atributo privado e retorna o valor

    def dar_like(self):
        self._likes += 1  # Acessa o atributo privado e modifica o valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programas):
    '''

    Herda atributos e métodos da classe programa e implementa duracao que é único dessa classe.
    Invoca os atributos da classe "Pai" através do método super()

    '''

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao #


class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


# Instanciando
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} | Likes: {vingadores.like}')


atlanta = Serie('atlanta', 2015, 8)
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} | Likes: {atlanta.like}')
