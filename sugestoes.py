import openai
api_key = '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'


def gerar_sugestoes(df):
    """Gera sugestões de texto a partir dos anúncios selecionados usando a chave de API especificada."""
    # Cria um objeto de compleção usando a chave de API da GPT-3

    # 3 opções de textos para o Google Ads com até 90 caracteres, com bons argumentos de venda semelhantes a esse: "Descubra o motivo de cada vez mais empresas virem para Sodexo. Melhores Benefícios.Acesse."
    completion = openai.Completion.create(
        engine="davinci",
        api_key=api_key,
    )
    sugestoes = []
    for _, row in df.iterrows():
        titulo = row['titulo']
        descricao = row['descricao']

        # Gera uma sugestão de texto usando a GPT-3
        prompt = f"{titulo}\n{descricao}"
        response = completion.complete(
            prompt=prompt,
            max_tokens=1024,
            temperature=0.7,
        )
        sugestao = response["choices"][0]["text"]

        # Adiciona a sugestão à lista
        sugestoes.append(sugestao)
    return sugestoes
