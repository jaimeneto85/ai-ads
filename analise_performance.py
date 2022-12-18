def atribuicao_de_nota(linha):
    nota = 0.0
    if linha['Performance'] == 'Bom':
        nota = 7.0
    elif linha['Performance'] == 'Aprendizado':
        nota = 6.0
    elif linha['Performance'] == 'Melhor':
        nota = 9.0
    elif linha['Performance'] == 'Baixa':
        nota = 4.0
    elif linha['Performance'] == 'Pendente':
        nota = 6.0

    if df.has_column('Impr.'):
        if linha['Impr.'] > linha['Impr.'].mean():
            nota += 1.0
        if linha['Impr.'] >= df['Impr.'].quantile(0.8):
            nota += 1.0

    return nota


def analise_dataframe(df):
    df['nota'] = df.apply(atribuicao_de_nota, axis=1)
