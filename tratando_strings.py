# TRATANDO STRING

frase = (str('   CUrso eM viDeo PytHon   '))
print('-' * 50)
print('String Original: {}'.format(frase))
print('-' * 50)

# FATIANDO
print('Split: ')
print(frase.split())
splt = (frase.split())
print('')

print('Posição 9 da String: [9]')
print(frase[9])
print('')

print('Da posição 9 até a 13: [9:14]')
print(frase[9:14])
print('')

print('Da Posição 9 a 13 Pulando de 2 em 2: [9:14:2]')
print(frase[9:14:2])
print('')

print('Da Posição 0 a 8: [:9]')
print(frase[:9])
print('')

print('Da Posição 9 ate o fim da string: [9:]')
print(frase[9:])
print('')

print('A partir da posição 9 pulando de 3 em 3: [9::3]')
print(frase[9::3])
print('')

# MODIFICANDO
print(frase.upper().strip())
print(frase.lower().strip())
print(frase.replace('CUrso', 'AULA').strip())
print(frase.title().strip())
print(frase.strip()) # REMOVE ESPAÇOS
print('*'.join(splt))
print('')

# ANALISANDO
print('Tamanho da String:')
print(len(frase))
print('')

print('Qtas ocorrencias da letra o:')
print(frase.count('o'))
print('')

# Conta ocorrências do 'o' da posição 0 ate a 12
print('Qtas ocorrencias da letra o da posição 0 até a 12:')
print(frase.count('o',0,13))
print('')

print('Procurando Deo:')
print(frase.find('Deo'))
print('')

# Procura termo 'Php', retorna valor -1 se não houver
print('Procura o termo Php, retorna valor -1 se não houver')
print(frase.find('Php'))
print('')

# Procura termo 'Curso', retorna boleano
print('Procura o termo CUrso, retorna boleano')
print('CUrso'in frase)
print('')

# Analisando String
name = str(input('Informe seu nome completo: ')).strip().title()
namesep = name.split()
print('')

print('Fist Name: {}'.format(namesep[0]))
print('Last Name: {}'.format(namesep[len(namesep) - 1]))
print('Seu nome tem {} Letras'.format(len(namesep[0])))
print('Seu nome tem Silva? {}'.format('silva' in name.lower())) #RETORNA BOOL
print('')

txt = str(input('Digite um texto qualquer: ')).strip().upper()
print('A letra A aparece {} vezes no texto.'.format(txt.count('A')))