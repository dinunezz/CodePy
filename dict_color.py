# COLORINDO TERMINAL COM ANSI
# Sintaxe: \033[ESTILO; COR_TEXTO; COR_BACKm

# ESTILO:
# 0 - Sem formtação
# 1 - Negrito
# 4 - Sublinhado
# 7 - Inverte Cores

#           COR_TEXTO     COR_BACK
# Branco        30          40
# Vermelho      31          41
# Verde         32          42
# Amarelo       33          43
# Azul          34          44
# Roxo          35          45
# Azul Claro    36          46
# Cinza         37          47

# Usando Dicionario de Cores

nome = 'Diego Nunes'
cores = {"limpa": "\033[m",
         "FundoBranco": "\033[40m",
         "FundoVerde": "\033[42m",
         "FundoAzul": "\033[44m",
         "LetraBranco": "\033[30m",
         "LetraVerde": "\033[32m",
         "LetraAzul": "\033[34m",
         "BrancaFverm": "\33[1;30;41m",
         "VermFBranco": "\33[1;31;40m",
         "LetraVerm": "\033[31m",
         }
print(type(cores))

print('Seja Bem-Vindo {} {} {}'.format(cores['FundoBranco'], nome, cores['limpa']))
print()
print('Seja Bem-Vindo {} {} {}'.format(cores['FundoVerde'], nome, cores['limpa']))
print()
print('Seja Bem-Vindo {} {} {}'.format(cores['FundoAzul'], nome, cores['limpa']))
print()
print('Seja Bem-Vindo {} {} {}'.format(cores['BrancaFverm'], nome, cores['limpa']))
print()
print('Seja Bem-Vindo {} {} {}'.format(cores['VermFBranco'], nome, cores['limpa']))
print()

print('Seja Bem-Vindo {} {} {}'.format(cores['LetraBranco'], nome, cores['limpa']))
print('Seja Bem-Vindo {} {} {}'.format(cores['LetraVerde'], nome, cores['limpa']))
print('Seja Bem-Vindo {} {} {}'.format(cores['LetraAzul'], nome, cores['limpa']))
print('Seja Bem-Vindo {} {} {}'.format(cores['LetraVerm'], nome, cores['limpa']))









