import openai
import streamlit as st

api_key = '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'
engine_name = "text-davinci-003"
openai.api_key = api_key
limite = {
    "Título": 30,
    "Título longo": 90,
    "Descrição": 90
}

def gerar_sugestoes(df):
    """Gera sugestões de texto a partir dos anúncios selecionados usando a chave de API especificada."""
    # Cria um objeto de compleção usando a chave de API da GPT-3
    # 3 opções de textos para o Google Ads com até 90 caracteres, com bons argumentos de venda semelhantes a esse: "Descubra o motivo de cada vez mais empresas virem para Sodexo. Melhores Benefícios.Acesse."
    sugestoes = []
    for _, row in df.iterrows():
        recurso = row['Recurso']
        tipo = row['Tipo de recurso']
        nota = row['nota']
        print('tipo... ', tipo)
        if not tipo in ['Título', 'Título longo', 'Titulo', 'Descrição']:
            st.write(f'Aidvisor ainda não está otimizado para {tipo}')
            continue
        # Gera uma sugestão de texto usando a GPT-3
        prompt = f"Utilizando as regras de anúncios do Google Ads (exemplo: não use caracteres especiais como '!'), crie um texto para anúncio no Google Ads. Com no máximo {limite[tipo]} caracteres. Sabendo que com bons argumentos de vendas semelhantes a esse: '{recurso}'"
        print('PROMPT : ', prompt)
        response = openai.Completion.create(
            engine=engine_name,
            prompt=prompt,
            max_tokens=limite[tipo],
            n=3,
            best_of=3,
            stop=None,
            temperature=0.7,
        )

        # sugestao = response["choices"][0]["text"]
        for index, choice in enumerate(response.choices):
            sugestao = {
                "Tipo de recurso": tipo,
                "Sugestao": choice.text.strip().replace("!", "."),
                # "logprobs": choice.logprobs
            }
            # Adiciona a sugestão à lista
            sugestoes.append(sugestao)
    return sugestoes
