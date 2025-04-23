# import pyrebase
import csv
import io
import re

import streamlit as st
import pandas as pd
from sugestoes import gerar_sugestoes
from download import baixar_sugestoes
from analise_performance import analise_dataframe

# Solicita o usuário e a senha do usuário
# with st.form(key='login', clear_on_submit=True):
#     login_input = st.sidebar.text_input("Usuário")
#     password_input = st.sidebar.text_input("Senha", type="password")
#     submit_button = st.sidebar.button("Login")

st.title("AI Ads - by @jaimeflneto")
st.text('Sua Inteligência Artificial para sugestão de conteúdo de alta performance!')


# Permite que o usuário selecione o arquivo CSV
st.subheader(
    'Acesse as variações de um anúncio e faça o download do arquivo em CSV e envie por aqui o resultado para receber sugestões de performance')
uploaded_file = st.file_uploader(
    "Selecione o arquivo CSV do Google Ads", type="csv")

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")

    corrected_content = io.StringIO()
    
    # Cria um leitor CSV para ler o conteúdo da string
    reader = csv.reader(io.StringIO(file_content), delimiter=',', quotechar='"')
    
    # Identifica se é um arquivo do Google Ads com linhas de metadados
    lines = list(reader)
    is_google_ads_format = False
    
    # Verifica se as primeiras linhas são metadados do Google Ads (em português ou inglês)
    first_line = ''.join(lines[0]) if lines and len(lines) > 0 else ""
    second_line = ''.join(lines[1]) if lines and len(lines) > 1 else ""
    
    # Padrões para detectar cabeçalhos do Google Ads em português e inglês
    pt_report_patterns = ["Relatório", "Detalhes"]
    en_report_patterns = ["Report", "Details"]
    
    # Meses em português e inglês
    pt_month_patterns = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
                         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    en_month_patterns = ["January", "February", "March", "April", "May", "June", 
                        "July", "August", "September", "October", "November", "December"]
    
    # Verifica se temos um relatório do Google Ads
    is_report_title = any(pattern in first_line for pattern in pt_report_patterns + en_report_patterns)
    has_date_format = (
        any(month in second_line for month in pt_month_patterns) or 
        any(month in second_line for month in en_month_patterns) or
        re.search(r'\d{1,2}/\d{1,2}/\d{4}', second_line) or  # DD/MM/YYYY or MM/DD/YYYY
        re.search(r'\d{4}-\d{1,2}-\d{1,2}', second_line)      # YYYY-MM-DD
    )
    
    if len(lines) > 2 and is_report_title and has_date_format:
        is_google_ads_format = True
        # Pula as duas primeiras linhas (metadados) e usa a linha 3 como cabeçalho
        header = lines[2]
        data_rows = lines[3:]
        
        # Escreve o cabeçalho
        corrected_content.write(','.join([val.replace(",", ";") for val in header]) + "\n")
        
        # Escreve as linhas de dados
        for linha in data_rows:
            if len(linha) < 3:
                # remove a linha incorreta
                continue
            linha = [val.replace(",", ";") for val in linha]
            new_line = ','.join(linha)
            corrected_content.write(new_line + "\n")
    else:
        # Processamento padrão para outros formatos CSV
        for linha in lines:
            if len(linha) < 3:
                # remove a linha incorreta
                continue
            linha = [val.replace(",", ";") for val in linha]
            new_line = ','.join(linha)
            corrected_content.write(new_line + "\n")

    # Reposiciona o ponteiro do buffer de string para o início
    corrected_content.seek(0)
    
    # Lê o arquivo CSV usando o pandas
    try:
        df = pd.read_csv(corrected_content)
    except Exception as e:
        st.error(f"Erro ao processar o arquivo CSV: {e}")
        st.write("Tente novamente com outro arquivo ou entre em contato com o suporte.")
        st.stop()
    
    # criar um novo arquivo para análisar o conteúdo e atribuir notas
    analise_dataframe(df)
    
    # Filtra os anúncios com nota acima de 7
    df = df[df['nota'] > 7]

    st.write('Melhores Recursos: ')
    st.dataframe(df)

    # Gera as sugestões
    sugestoes = gerar_sugestoes(df)

    # Exibe as sugestões em uma tabela
    st.dataframe(sugestoes)

    # Cria um botão de download
    st.button("Processar novamente!")
    # Baixa as sugestões
    baixar_sugestoes(sugestoes)
