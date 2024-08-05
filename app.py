# import pyrebase
import csv
import io

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
    # print('READEr ', io.StringIO(file_content).getvalue())
    for linha in reader:
        if len(linha) < 3:
            # remove a linha incorreta
            continue
        linha = [val.replace(",", ";" ) for val in linha]
        new_line = ','.join(linha)
        corrected_content.write(new_line + "\n")

    # Reposiciona o ponteiro do buffer de string para o início
    corrected_content.seek(0)
    # Lê o arquivo CSV usando o pandas
    df = pd.read_csv(corrected_content,  error_bad_lines=False)
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
