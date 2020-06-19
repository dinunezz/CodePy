def color(cor):
    """
    Função para colorir as saídas no terminal
    :param cor:
    # LIMPA FORMATAÇÃO:
    "limpa"

    # FUNDOS:
    "FdBranco"
    "FdVerm"
    "FdVerde"
    "FdAmarelo"
    "FdAzul"
    "FdRoxo"
    "FdAzulClaro"
    "FdCinza"

    # LETRAS:
    "LtBranca"
    "LtVerm"
    "LtVerde"
    "LtAmarelo"
    "LtAzul"
    "LtRoxo"
    "LtAzulClaro"
    "LtCinza"

    # LETRA + FUNDO:
    "LtBrancaFdVerm"
    "LtVermFdBranco"
    "LtBrancaFdAzul"

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

    :return:
    """
    #LIMPA FORMATAÇÃO
    if cor == "limpa":
        return "\033[m"
    #FUNDOS
    elif cor == "FdBranco":
        return "\033[40m"
    elif cor == "FdVerm":
        return "\033[41m"
    elif cor == "FdVerde":
        return "\033[42m"
    elif cor == "FdAmarelo":
        return "\033[1;37;43m"
    elif cor == "FdAzul":
        return "\033[44m"
    elif cor == "FdRoxo":
        return "\033[45m"
    elif cor == "FdAzulClaro":
        return "\033[46m"
    elif cor == "FdCinza":
        return "\033[47m"
    #LETRAS
    elif cor == "LtBranca":
        return "\033[30m"
    elif cor == "LtVerm":
        return "\033[31m"
    elif cor == "LtVerde":
        return "\033[32m"
    elif cor == "LtAmarelo":
        return "\033[33m"
    elif cor == "LtAzul":
        return "\033[34m"
    elif cor == "LtRoxo":
        return "\033[35m"
    elif cor == "LtAzulClaro":
        return "\33[36m"
    elif cor == "LtCinza":
        return "\33[37m"
    #LETRA + FUNDO
    elif cor == "LtBrancaFdVerm":
        return "\33[1;30;41m"
    elif cor == "LtVermFdBranco":
        return "\33[1;31;40m"
    elif cor == "LtBrancaFdAzul":
        return "\33[1;30;44m"
