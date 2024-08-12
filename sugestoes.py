import openai
import streamlit as st
from dotenv import load_dotenv
import os

api_key = os.getenv("API_KEY")
engine_name = os.getenv("ENGINE_NAME")
openai.api_key = api_key
limite = {
    "Título": 30,
    "Título longo": 90,
    "Descrição": 90,
    "Headline": 30,
    "Description": 90,
}

def gerar_sugestoes(df):
    """Gera sugestões de texto a partir dos anúncios selecionados usando a chave de API especificada."""
    sugestoes = []
    for _, row in df.iterrows():
        recurso = row['Recurso']
        tipo = row['Tipo de recurso']
        nota = row['nota']
        print('tipo... ', tipo)
        if not tipo in ['Título', 'Título longo', 'Titulo', 'Descrição']:
            st.write(f'AI-Ads ainda não está otimizado para {tipo}')
            continue

        prompt = f"Atue como especialista em anúncios do Google Ads. Utilizando as regras de anúncios do Google Ads (exemplo: não use caracteres especiais como '!'), crie um texto para anúncio no Google Ads. Com no máximo {limite[tipo]} caracteres. Sabendo que com bons argumentos de vendas semelhantes a esse: '{recurso}'"
        
        response = openai.Completion.create(
            engine=engine_name,
            prompt=prompt,
            max_tokens=limite[tipo],
            n=3,
            best_of=3,
            stop=None,
            temperature=0.7,
        )

        for index, choice in enumerate(response.choices):
            sugestao = {
                "Tipo de recurso": tipo,
                "Sugestao": choice.text.strip().replace("!", "."),
            }
            # Adiciona a sugestão à lista
            sugestoes.append(sugestao)
    return sugestoes
