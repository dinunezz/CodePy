def fecharTicket(dias=0):
    '''
    :param dias: qtde de dias a subtrair
    :return: retorna a data passada subtraindo os dias a partir da data de hoje.
    '''
    from datetime import date
    dtHoje = date.today()
    dtLimite = date.fromordinal(dtHoje.toordinal() - dias)
    print('Fechar chamados anteriores há: {}/{}/{}'.format(dtLimite.day, dtLimite.month, dtLimite.year))


fecharTicket()