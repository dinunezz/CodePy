from random import choice

upper = ["B", "C", "D", "F", "G", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "&", "*"]

qtd = (int(input('Quantas Sugestões De Senhas Deseja Gerar? ')))

for c in range(qtd):
    print('=*=' * 6)
    print(f'Senha {c+1}:'
          f' {choice(upper)}'
          f'{choice(lower)}'
          f'{choice(lower)}'
          f'{choice(numbers)}'
          f'{choice(numbers)}'
          f'{choice(numbers)}'
          f'{choice(numbers)}'
          f'{choice(symbols)}')
    c += 1
print('=*=' * 6)
